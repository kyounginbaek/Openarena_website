# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-26 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_auto_20161126_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundingdummy',
            name='thankyou',
        ),
        migrations.AddField(
            model_name='funding',
            name='reward',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 818816, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 817847, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 819376, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 821906, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 820749, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 26, 9, 26, 57, 821254, tzinfo=utc), max_length=40),
        ),
    ]
