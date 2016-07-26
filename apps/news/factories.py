# coding: utf-8
import datetime
import factory

from apps.news.models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: u"article%s" % n)
    url = factory.Sequence(lambda n: u"http://hackernews.com/%s" % n)
    published_at = factory.LazyAttribute(lambda o: datetime.datetime.now())

    class Meta:
        model = Article
