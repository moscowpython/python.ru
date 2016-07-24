from django.db import models
from django.db.models import QuerySet
from model_utils import Choices
from model_utils.models import TimeStampedModel


class ArticleQuerySet(QuerySet):

    def active(self):
        return self.filter(is_active=True)


class Article(TimeStampedModel):
    url = models.URLField('URL')
    name = models.CharField('Заголовок', max_length=1024)
    description = models.TextField('Описание', blank=True)
    published_at = models.DateTimeField('Дата публикации')
    source = models.CharField('Источник', max_length=32, choices=Choices('pythondigest',))
    external_id = models.CharField('Внешний ID', max_length=32, unique=True, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение', blank=True, upload_to='articles')
    is_active = models.BooleanField('Показывать на сайте', default=True)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at', '-id']
