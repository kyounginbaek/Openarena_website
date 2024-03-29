# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-01 06:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0082_auto_20161129_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 585496, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 584508, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 586094, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 588742, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 587540, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 1, 6, 24, 26, 588070, tzinfo=utc), max_length=40),
        ),
    ]
