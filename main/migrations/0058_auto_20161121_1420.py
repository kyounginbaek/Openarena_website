# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-21 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_auto_20161121_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='thankyou',
            field=models.IntegerField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='fundingdummy',
            name='thankyou',
            field=models.IntegerField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='amount',
            field=models.IntegerField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 450535, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='amount',
            field=models.IntegerField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 449539, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='confirm',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 451080, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 453649, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='reply',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 452440, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 11, 21, 5, 20, 38, 452977, tzinfo=utc), max_length=40),
        ),
    ]