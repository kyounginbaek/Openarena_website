# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-24 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0146_auto_20170223_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='file',
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='file_profile',
            field=models.FileField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='file_tournament',
            field=models.FileField(blank=True, null=True, upload_to='tournament'),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 6, 6, 48, 398238, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 6, 6, 48, 395916, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 6, 6, 48, 399179, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 6, 6, 48, 406810, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 6, 6, 48, 405852, tzinfo=utc), max_length=40),
        ),
    ]
