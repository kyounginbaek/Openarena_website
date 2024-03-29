# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-17 11:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0141_auto_20170217_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 17, 11, 29, 5, 559049, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 17, 11, 29, 5, 557011, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 17, 11, 29, 5, 559965, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 17, 11, 29, 5, 567767, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 17, 11, 29, 5, 566680, tzinfo=utc), max_length=40),
        ),
    ]
