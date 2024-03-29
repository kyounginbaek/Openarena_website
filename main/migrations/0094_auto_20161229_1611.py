# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-29 07:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0093_auto_20161229_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 29, 7, 11, 3, 832577, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 29, 7, 11, 3, 831631, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='description',
            field=models.TextField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 29, 7, 11, 3, 833313, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 29, 7, 11, 3, 835509, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 29, 7, 11, 3, 834824, tzinfo=utc), max_length=40),
        ),
    ]
