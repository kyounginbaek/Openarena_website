# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 08:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0099_auto_20170106_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='agreement',
            new_name='contents',
        ),
        migrations.RenameField(
            model_name='privacy',
            old_name='privacy',
            new_name='contents',
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 43, 9, 194087, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 43, 9, 193051, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 43, 9, 194693, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 43, 9, 196983, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 43, 9, 196250, tzinfo=utc), max_length=40),
        ),
    ]
