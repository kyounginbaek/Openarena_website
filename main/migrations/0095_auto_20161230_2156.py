# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0094_auto_20161229_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 30, 12, 56, 8, 681390, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 30, 12, 56, 8, 679984, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 30, 12, 56, 8, 682298, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 30, 12, 56, 8, 684351, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 12, 30, 12, 56, 8, 683667, tzinfo=utc), max_length=40),
        ),
    ]
