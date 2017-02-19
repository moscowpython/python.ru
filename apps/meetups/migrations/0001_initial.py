# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-14 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20170214_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=256)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Место работы',
                'verbose_name_plural': 'Места работы',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('contact_url', models.CharField(blank=True, max_length=256, null=True)),
                ('avatar', models.ImageField(upload_to='speaker_avatars')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers', to='meetups.Employer')),
            ],
            options={
                'verbose_name': 'Докладчик',
                'verbose_name_plural': 'Докладчики',
            },
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('slides_url', models.CharField(blank=True, max_length=256, null=True)),
                ('video_url', models.CharField(blank=True, max_length=256, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='events.Event')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='meetups.Speaker')),
            ],
            options={
                'verbose_name': 'Доклад',
                'verbose_name_plural': 'Доклады',
            },
        ),
    ]
