# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-16 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170219_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place_and_time_html',
            field=models.TextField(blank=True, null=True),
        ),
    ]