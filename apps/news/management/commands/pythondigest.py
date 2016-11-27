import datetime
import hashlib
import logging
import os
from itertools import chain

import bleach
import feedparser
import requests
from dateutil import parser
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.timezone import make_aware
from lxml.html import fromstring

from apps.news.models import Article


logger = logging.getLogger('management.pythondigest')


class Command(BaseCommand):
    help = 'Imports feed from pythondigest'

    def add_arguments(self, parser):
        parser.add_argument(
            '--update',
            action='store_true',
            default=False,
            help='Update existing articles data',
        )
        parser.add_argument(
            '--update-images',
            action='store_true',
            default=False,
            help='Update existing articles images',
        )
        parser.add_argument(
            '--date',
            help='Fetch json API for specific date instead of RSS',
        )
        parser.add_argument(
            '--days',
            help='Fetch json API fro N days',
        )
        parser.add_argument(
            '--till-date',
            help='Fetch json API till specific date via API',
        )

    def handle(self, *args, **options):
        if options['date']:
            feed = pydigest_articles_for_date(parser.parse(options['date']))
        elif options['days']:
            till_date = parser.parse(options['till_date']) if options['till_date'] else datetime.datetime.now()
            daterange = (till_date - datetime.timedelta(days=offset) for offset in range(int(options['days'])))
            feed = chain.from_iterable(pydigest_articles_for_date(dt) for dt in daterange)
        else:
            feed = pydigest_article_feed()

        for article_data, image_bytes in feed:
            try:
                if options['update']:
                    external_id = article_data.pop('external_id')
                    article, _ = Article.objects.update_or_create(
                        external_id=external_id, defaults=article_data,
                    )
                else:
                    article = Article.objects.create(**article_data)
                if image_bytes and options['update_images']:
                    article.image.save('cover-%s.jpg' % article.id, ContentFile(image_bytes))
            except IntegrityError:
                logger.info(self.style.NOTICE('Already existing article "%s"' % article_data['name']))
            else:
                logger.info(self.style.SUCCESS('Fetched article "%s"' % article.name))


def download_image(url):
    if not url:
        return
    logger.info('Fetching image %s', url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.exception('Failed to fetch image %s', url)


def fetch_image_from_summary(html):
    image_bytes = None
    if not html:
        return image_bytes, html
    doc = fromstring(html)
    for img in doc.xpath('//img'):
        src = img.get('srcset')
        if not src:
            continue
        image_bytes = download_image('https://pythondigest.ru/' + src)
    return image_bytes, html


def clean_html(html):
    return bleach.clean(html, tags=['p', 'a'], strip=True)


def get_page_metadata(url):
    token = os.environ.get('MERCURY_PARSER_KEY', None)
    if not token:
        return {}
    try:
        # Docs: https://mercury.postlight.com/web-parser/
        session = requests.session()
        session.headers.update({
            'x-api-key': os.environ.get('MERCURY_PARSER_KEY'),
            'User-Agent': 'PythonRuFetcher/1.0 +https://python.ru/'
        })
        return session.get('https://mercury.postlight.com/parser', params={'url': url}).json()
    except Exception:
        logger.exception('Failed to parse data for url %s', url)


def pydigest_article_feed():
    feed = feedparser.parse('https://pythondigest.ru/rss/',
                            agent='PythonRuFetcher/1.0 +https://python.ru/')
    for item in feed.entries:
        image_bytes, summary = fetch_image_from_summary(item['summary'])
        yield dict(
            url=item['link'],
            name=item['title'],
            description=clean_html(summary),
            published_at=parser.parse(item['published']),
            external_id=hashlib.md5(item['id'].encode('utf-8')).hexdigest(),
            source='pythondigest',
        ), image_bytes


def pydigest_articles_for_date(date):
    response = requests.get('https://pythondigest.ru/api/items/{year}/{month}/{day}/'.format(
        year=date.year, month=date.month, day=date.day
    ), headers={'User-Agent': 'PythonRuFetcher/1.0 +https://python.ru/'})
    if not response.json()['ok']:
        logger.info('No stuff found')
        return

    for item in response.json()['items']:
        image_bytes, summary = fetch_image_from_summary(item['description'])
        extra_metadata = get_page_metadata(item['link'])

        # fall back to readability data
        summary = clean_html(summary) or clean_html(extra_metadata.get('excerpt', ''))
        # fetch lead image from source
        image_bytes = image_bytes or download_image(extra_metadata.get('lead_image_url', None))

        yield dict(
            url=item['link'],
            name=item['title'],
            description=clean_html(summary),
            published_at=make_aware(datetime.datetime.combine(date, datetime.datetime.min.time())),
            language=item['language'],
            section=item['section__title'],
            external_id=hashlib.md5(item['link'].encode('utf-8')).hexdigest(),
            source='pythondigest'
        ), image_bytes
