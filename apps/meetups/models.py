from django.db import models
from model_utils.models import TimeStampedModel


class Employer(TimeStampedModel):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работы'


class Speaker(TimeStampedModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    contact_url = models.CharField(max_length=256, null=True, blank=True)
    avatar = models.ImageField(upload_to='speaker_avatars')
    employer = models.ForeignKey('Employer', related_name='speakers')

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Докладчик'
        verbose_name_plural = 'Докладчики'


class Talk(TimeStampedModel):
    event = models.ForeignKey('events.Event', related_name='talks')
    speaker = models.ForeignKey('Speaker', related_name='talks')
    title = models.CharField(max_length=256)
    description = models.TextField()
    slides_url = models.CharField(
        max_length=256, null=True, blank=True,
        help_text='Айфрейм можно получить iframely.com',
    )
    video_url = models.CharField(
        max_length=256, null=True, blank=True,
        help_text='Лучше удалить атрибуты height и width у айфрейма'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доклад'
        verbose_name_plural = 'Доклады'
