# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-16 11:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0122_auto_20170116_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 16, 11, 20, 0, 173735, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 16, 11, 20, 0, 172618, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='help',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='making',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='making',
            name='notice',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 16, 11, 20, 0, 174385, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 16, 11, 20, 0, 176837, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='privacy',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 16, 11, 20, 0, 176010, tzinfo=utc), max_length=40),
        ),
    ]
