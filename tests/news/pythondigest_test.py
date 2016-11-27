# coding: utf-8
import datetime
import vcr
from django.core.management import call_command
from django.utils.timezone import utc

from apps.news.management.commands.pythondigest import get_page_metadata
from apps.news.models import Article

my_vcr = vcr.VCR(
    cassette_library_dir='tests/cassettes',
    record_mode='once',
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    decode_compressed_response=True
)


@my_vcr.use_cassette
def test_pythondigest(db):
    call_command('pythondigest')

    assert Article.objects.count() == 10

    article = Article.objects.order_by('-published_at', 'id').last()
    assert article.url == 'http://github.com/PokemonGoF/PokemonGo-Bot'
    assert article.name == 'PokemonGo-Bot - бот для поиска покемонов'
    assert article.description == ''
    assert article.published_at == datetime.datetime(2016, 7, 24, 11, 1, 36, tzinfo=utc)
    assert not article.is_active
    assert not article.is_featured
    assert article.source == 'pythondigest'

    article = Article.objects.order_by('-published_at', 'id').first()
    assert article.description == '<p>Плейлист с видео с конференции SciPy 2016</p>'


@my_vcr.use_cassette
def test_pythondigest_daterange(db):
    call_command('pythondigest', days=2, till_date='2016-10-29')

    assert Article.objects.count() == 2


@my_vcr.use_cassette
def test_get_page_metadata(monkeypatch):
    url = 'https://semaphoreci.com/community/tutorials/setting-up-a-bdd-stack-on-a-django-application'
    metadata = get_page_metadata(url)
    assert metadata == {}

    monkeypatch.setenv('MERCURY_PARSER_KEY', 'xxx')
    metadata = get_page_metadata(url)
    assert metadata['excerpt'].startswith('Boost your Django and Python stack with Behavior Driven Development.')
    assert metadata['lead_image_url'].startswith('https://d1dkupr86d302v.cloudfront.net/')
