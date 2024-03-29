# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-08 08:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0101_auto_20170106_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(default='', max_length=20)),
                ('question', models.CharField(default='', max_length=100)),
                ('answer', django_summernote.fields.SummernoteTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 18, 12, 968926, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 18, 12, 967968, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 18, 12, 969482, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 18, 12, 971562, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 8, 8, 18, 12, 970908, tzinfo=utc), max_length=40),
        ),
    ]
