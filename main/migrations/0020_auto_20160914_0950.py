# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 00:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20160914_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 9, 14, 0, 50, 42, 247935, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 9, 14, 0, 50, 42, 248875, tzinfo=utc), max_length=40),
        ),
    ]
