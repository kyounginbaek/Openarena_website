# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-08 08:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0102_auto_20170108_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='number',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 29, 18, 252044, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 29, 18, 251086, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 29, 18, 252606, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 29, 18, 254699, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 29, 18, 254045, tzinfo=utc), max_length=40),
        ),
    ]
