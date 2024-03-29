# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-07 06:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0181_auto_20170405_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tournament_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 6, 11, 50, 643259, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 6, 11, 50, 641959, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 6, 11, 50, 643884, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 6, 11, 50, 648125, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 4, 7, 6, 11, 50, 647424, tzinfo=utc), max_length=400),
        ),
    ]
