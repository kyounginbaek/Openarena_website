# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-15 07:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0154_auto_20170315_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 15, 7, 30, 23, 530033, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 15, 7, 30, 23, 527830, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 15, 7, 30, 23, 530827, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 15, 7, 30, 23, 535117, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='funding_endtime',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='funding_goal',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='funding_starttime',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='funding_time',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_checkin',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_custom_url',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_endtime',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_number',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_starttime',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_template',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_template_custom',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_template_format',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_time',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_type',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise_number',
            field=models.CharField(default='-', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise_spec',
            field=models.CharField(default='-', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward_number',
            field=models.CharField(default='-', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward_spec',
            field=models.CharField(default='-', max_length=4000),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 15, 7, 30, 23, 534381, tzinfo=utc), max_length=400),
        ),
    ]
