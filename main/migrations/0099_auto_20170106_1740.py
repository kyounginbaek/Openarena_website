# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0098_auto_20170106_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 40, 29, 981202, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 40, 29, 980237, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 40, 29, 981763, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 40, 29, 983838, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='privacy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 40, 29, 983158, tzinfo=utc), max_length=40),
        ),
    ]
