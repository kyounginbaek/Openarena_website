# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-01 05:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20161101_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 1, 5, 42, 15, 516935, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='streaming_url_spec',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 1, 5, 42, 15, 517883, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participant',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 1, 5, 42, 15, 520518, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 1, 5, 42, 15, 519255, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 1, 5, 42, 15, 519812, tzinfo=utc), max_length=40),
        ),
    ]
