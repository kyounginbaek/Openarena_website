# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-02 07:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0135_auto_20170130_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 2, 7, 22, 44, 116096, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 2, 7, 22, 44, 114239, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 2, 7, 22, 44, 116732, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 2, 7, 22, 44, 120317, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 2, 7, 22, 44, 119580, tzinfo=utc), max_length=40),
        ),
    ]
