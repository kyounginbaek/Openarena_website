# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-13 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20161113_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='etc4',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 164814, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 165770, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 166309, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 168868, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 167584, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 13, 8, 50, 1, 168202, tzinfo=utc), max_length=40),
        ),
    ]
