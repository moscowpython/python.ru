from django.db import models
from django.utils import timezone


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название места где будет размещатся банер')
    tag = models.CharField(max_length=10, verbose_name='id где будет размещатся банер')

    def __str__(self):
        return 'Расположение {}'.format(self.name)

    class Meta:
        verbose_name = "Расположение"
        verbose_name_plural = "Расположение баннеров"


class Banner(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название баннера',
                            help_text='Назовите баннер так, чтобы было удобно в дальнейшем '
                                      'определять его среди других баннеров')
    file_swf = models.FileField(upload_to='data/', verbose_name='Swf-файл', blank=True, null=True)
    file_img = models.FileField(upload_to='data-img/', verbose_name='Файл изображения', blank=True, null=True)
    width = models.CharField(max_length=7, blank=True, verbose_name='Ширина отображения баннера',
                             help_text='Например, 100px, 720px или 100%')
    height = models.CharField(max_length=7, blank=True, verbose_name='Высота отображения баннера',
                              help_text='Например, 100px, 200px или 100%')
    link_to = models.CharField(max_length=255, blank=False, verbose_name='Ссылка перехода',
                               help_text='Главная ссылка перехода.')
    date_from = models.DateField(default=timezone.now, verbose_name='Дата старта показа баннеров', help_text='')
    date_to = models.DateField(verbose_name='Дата окончания показа баннеров', help_text='В эту дату ещё будут показы.')
    date_days = models.IntegerField(default=254, verbose_name='Дни недели для показа',
                                    help_text='Вычисляется как сумма: Понедельник = 2, Вторник = 4, Среда = 8, '
                                              'Четверг = 16, Пятница = 32, Суббота = 64, Воскресенье = 128. '
                                              'Для всей недели = 254, Только выходные = 192, Только будни = 62')
    date_time_from = models.IntegerField(default=0, verbose_name='Час начала показа каждый указанный день',
                                         help_text='Например, 12 или 20')
    date_time_to = models.IntegerField(default=24, verbose_name='Час окончания показа каждый указанный день',
                                       help_text='Не может быть меньше, чем час начала. Например, 12 или 20')
    priority = models.IntegerField(verbose_name='Приоритет показа от 1 до 100', help_text='')
    position = models.ForeignKey(Position, verbose_name='Место размещение банера', on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='Активность баннера')

    def __str__(self):
        return u'Баннер {}'.format(self.name)

    def __unicode__(self):
        return u'#{} {}'.format(self.id, self.name)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
