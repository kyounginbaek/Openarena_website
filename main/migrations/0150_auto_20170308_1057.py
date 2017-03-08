# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 01:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0149_auto_20170227_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tournament_format',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_format_spec',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_format_spec_detail',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 1, 57, 40, 931105, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 1, 57, 40, 929297, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 1, 57, 40, 931912, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 1, 57, 40, 936553, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 8, 1, 57, 40, 935737, tzinfo=utc), max_length=400),
        ),
    ]
