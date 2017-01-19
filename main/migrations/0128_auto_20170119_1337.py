# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-19 04:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0127_auto_20170117_2045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fundingdummy',
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 19, 4, 37, 21, 257122, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 19, 4, 37, 21, 258108, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 19, 4, 37, 21, 260431, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 19, 4, 37, 21, 259679, tzinfo=utc), max_length=40),
        ),
    ]
