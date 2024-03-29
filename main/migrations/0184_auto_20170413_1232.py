# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-13 03:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0183_auto_20170410_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='seed',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 242957, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 241722, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 243553, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 247646, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 244860, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 3, 32, 16, 246947, tzinfo=utc), max_length=400),
        ),
    ]
