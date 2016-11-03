# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-02 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20161101_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 5, 27, 33, 956935, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 5, 27, 33, 957826, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participant',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 5, 27, 33, 960477, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 5, 27, 33, 959173, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 5, 27, 33, 959729, tzinfo=utc), max_length=40),
        ),
    ]
