# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-15 10:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0188_auto_20170415_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 316378, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 314397, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 317016, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 321540, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 318384, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 15, 10, 17, 21, 320782, tzinfo=utc), max_length=400),
        ),
    ]
