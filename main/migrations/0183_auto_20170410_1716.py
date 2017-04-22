# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-10 08:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0182_auto_20170407_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='confirm',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 10, 8, 16, 13, 432223, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 10, 8, 16, 13, 428162, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 10, 8, 16, 13, 433424, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 10, 8, 16, 13, 442343, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 10, 8, 16, 13, 440902, tzinfo=utc), max_length=400),
        ),
    ]