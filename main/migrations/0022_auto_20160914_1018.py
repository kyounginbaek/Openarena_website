# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 01:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160914_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 9, 14, 1, 18, 24, 682829, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 9, 14, 1, 18, 24, 683684, tzinfo=utc), max_length=40),
        ),
    ]
