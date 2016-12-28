# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-05 06:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0083_auto_20161201_1524'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='thankyou',
        ),
        migrations.AddField(
            model_name='funding',
            name='thanks',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='funding',
            name='comment',
            field=models.TextField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='funding',
            name='orderno',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='reward',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 51, 52, 496825, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 51, 52, 495878, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 51, 52, 497377, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='checkin',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='participation',
            name='confirm',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='participation',
            name='etc1',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='etc2',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='etc3',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='etc4',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='prize',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='result',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='score',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='teammember',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='participation',
            name='teamname',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 51, 52, 502662, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 51, 52, 501311, tzinfo=utc), max_length=40),
        ),
    ]
