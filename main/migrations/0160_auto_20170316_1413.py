# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-16 05:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0159_auto_20170316_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 16, 5, 13, 36, 66236, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 16, 5, 13, 36, 65020, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='checkin',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='checkin_time',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='confirm',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='email',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='funding_endtime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='funding_goal',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='participant',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='participation_endtime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='registration',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='registration_team',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='starttime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='streaming_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='streaming_url_spec',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='template',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='tournament_game',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='tournament_name',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='tournament_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='making',
            name='username',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 16, 5, 13, 36, 66793, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 16, 5, 13, 36, 70710, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 16, 5, 13, 36, 70014, tzinfo=utc), max_length=400),
        ),
    ]
