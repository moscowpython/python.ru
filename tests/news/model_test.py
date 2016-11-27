# coding: utf-8
import pytest

from apps.news.factories import ArticleFactory
from apps.news.models import Article


@pytest.mark.django_db
def test_featured():
    assert Article.objects.featured() is None

    article = ArticleFactory()
    assert Article.objects.featured() == article

    really_featured = ArticleFactory(is_featured=True)
    assert Article.objects.featured() == really_featured
