# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-14 05:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0185_auto_20170413_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='chollonge_start',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 37091, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 35828, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 37672, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 42133, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 39278, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 5, 23, 1, 41423, tzinfo=utc), max_length=400),
        ),
    ]
