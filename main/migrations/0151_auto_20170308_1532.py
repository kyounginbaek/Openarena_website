# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0150_auto_20170308_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 6, 32, 29, 513808, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 6, 32, 29, 512780, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 6, 32, 29, 514557, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 6, 32, 29, 518656, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 6, 32, 29, 517943, tzinfo=utc), max_length=400),
        ),
    ]
