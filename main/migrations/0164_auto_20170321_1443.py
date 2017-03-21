# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-21 05:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0163_auto_20170317_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 21, 5, 43, 14, 597532, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 21, 5, 43, 14, 596108, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 21, 5, 43, 14, 598930, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 21, 5, 43, 14, 605480, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='confirm',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='cover_image',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='logo_image',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_template',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participation_template_format',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise_number',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise_spec',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward_number',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward_spec',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 21, 5, 43, 14, 603941, tzinfo=utc), max_length=400),
        ),
    ]