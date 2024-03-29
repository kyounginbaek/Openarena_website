# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-31 02:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0172_auto_20170330_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participation',
            old_name='etc6',
            new_name='input',
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 31, 2, 3, 59, 691642, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 31, 2, 3, 59, 690100, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 31, 2, 3, 59, 692417, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 31, 2, 3, 59, 699202, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 31, 2, 3, 59, 697517, tzinfo=utc), max_length=400),
        ),
    ]
