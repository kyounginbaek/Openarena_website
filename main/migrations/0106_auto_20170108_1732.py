# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-08 08:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0105_auto_20170108_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 32, 21, 605329, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 32, 21, 604012, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 32, 21, 605989, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 32, 21, 608303, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 32, 21, 607530, tzinfo=utc), max_length=40),
        ),
    ]