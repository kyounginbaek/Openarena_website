# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-17 12:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20161117_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 837705, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 838690, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 839219, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 841833, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 840495, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 17, 12, 16, 13, 841124, tzinfo=utc), max_length=40),
        ),
    ]
