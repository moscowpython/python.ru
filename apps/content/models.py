from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Link(TimeStampedModel):
    SECTIONS = Choices(
        ('courses', 'Обучающие курсы'),
        ('docs', 'Документация'),
        ('community', 'Сообщество'))
    SECTION_SLUGS = [slug for slug, value in SECTIONS]

    url = models.URLField('URL')
    name = models.CharField('Название ссылки', max_length=256)
    section = models.CharField(u'Рубрика', choices=SECTIONS, max_length=20)
    order = models.IntegerField(u'Порядок', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['section', 'order', '-id']


class Slider(TimeStampedModel):
    """Main slider in top page."""
    top_badge = models.CharField('значок в верхней части', max_length=32)
    color = models.CharField('Background color', max_length=32)
    logo = models.CharField('Логотип', max_length=140)
    title = models.CharField('Заголовок слайда', max_length=140)
    is_visible = models.BooleanField('Видимость слайда', default=True)
    date = models.CharField('Дата проведение проекта', max_length=140)
    description = models.CharField('Описание проекта', max_length=300)
