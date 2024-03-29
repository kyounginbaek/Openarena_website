# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-07 02:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0136_auto_20170202_1622'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rule',
            new_name='Gamerule',
        ),
        migrations.AddField(
            model_name='tournament',
            name='participation_checkintime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='participation_date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='registration',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_endtime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_starttime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 2, 52, 55, 94397, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 2, 52, 55, 93197, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 2, 52, 55, 95044, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 2, 52, 55, 98675, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 2, 52, 55, 97942, tzinfo=utc), max_length=40),
        ),
    ]
