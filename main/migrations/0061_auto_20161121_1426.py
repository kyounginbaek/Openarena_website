# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-21 05:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_auto_20161121_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 242228, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 241196, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 242786, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 245412, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 244200, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 26, 16, 244736, tzinfo=utc), max_length=40),
        ),
    ]