from django.db import models
from django.db.models import QuerySet
from model_utils.models import TimeStampedModel
import datetime


class City(TimeStampedModel):
    name = models.CharField('Название города', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['-id']


class EventQuerySet(QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def upcoming(self):
        return self.active().filter(date__date__gte=datetime.datetime.today().date())


class Event(TimeStampedModel):
    name = models.CharField('Название события', max_length=256)
    city = models.ForeignKey(City)
    date = models.DateTimeField('Начало события', blank=True, null=True)
    is_active = models.BooleanField('Отображается на сайте', default=True)
    url = models.URLField('Ссылка на событие', blank=True)

    objects = EventQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['date', '-id']
