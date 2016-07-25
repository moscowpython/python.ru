import hashlib

import bleach
import feedparser
import requests
from dateutil import parser
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from lxml.html import fromstring

from apps.news.models import Article


class Command(BaseCommand):
    help = 'Imports feed from pythondigest'

    def add_arguments(self, parser):
        parser.add_argument(
            '--update',
            action='store_true',
            default=False,
            help='Delete article and replace with new one',
        )
        parser.add_argument(
            '--update-images',
            action='store_true',
            default=False,
            help='Delete article and replace with new one',
        )

    def handle(self, *args, **options):
        for article_data, image_bytes in pydigest_article_feed():
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
                self.stdout.write(self.style.NOTICE('Already existing article "%s"' % article_data['name']))
            else:
                self.stdout.write(self.style.SUCCESS('Fetched article "%s"' % article.name))


def fetch_image_from_summary(html):
    image_bytes = None
    if not html:
        return image_bytes, html
    doc = fromstring(html)
    for img in doc.xpath('//img'):
        src = img.get('srcset')
        if not src:
            continue
        try:
            response = requests.get('https://pythondigest.ru/' + src)
            response.raise_for_status()
            image_bytes = response.content
        except requests.RequestException as e:
            pass
    return image_bytes, html


def clean_html(html):
    return bleach.clean(html, tags=['p', 'a'], strip=True)


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
        ), image_bytes
