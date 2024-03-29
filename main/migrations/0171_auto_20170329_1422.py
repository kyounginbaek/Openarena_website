# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-29 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0170_auto_20170327_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 29, 5, 22, 48, 556771, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 29, 5, 22, 48, 555469, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 29, 5, 22, 48, 557417, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 29, 5, 22, 48, 561658, tzinfo=utc), max_length=400),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='notice',
            field=django_summernote.fields.SummernoteTextField(default='-'),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 3, 29, 5, 22, 48, 560940, tzinfo=utc), max_length=400),
        ),
    ]
