# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('url', models.URLField(verbose_name='URL')),
                ('name', models.CharField(max_length=256, verbose_name='Название ссылки')),
                ('section', models.CharField(choices=[('courses', 'Обучающие курсы'), ('docs', 'Документация'), ('community', 'Сообщество')], max_length=20, verbose_name='Рубрика')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'ordering': ['section', 'order', '-id'],
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
