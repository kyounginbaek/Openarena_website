# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0100_auto_20170106_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='contents',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='privacy',
            old_name='contents',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 53, 7, 427659, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 53, 7, 426681, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 53, 7, 428225, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 53, 7, 430303, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 53, 7, 429654, tzinfo=utc), max_length=40),
        ),
    ]
