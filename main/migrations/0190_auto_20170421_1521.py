# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-21 06:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0189_auto_20170415_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 57, 1750, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 56, 999519, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 57, 2345, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 57, 8584, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 57, 4351, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 21, 6, 21, 57, 7523, tzinfo=utc), max_length=400),
        ),
    ]