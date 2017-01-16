# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 08:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_auto_20170105_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement', django_summernote.fields.SummernoteTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy', django_summernote.fields.SummernoteTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 36, 48, 846379, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 36, 48, 845282, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 36, 48, 846999, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 36, 48, 849219, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 6, 8, 36, 48, 848526, tzinfo=utc), max_length=40),
        ),
    ]