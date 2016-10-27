# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 17:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20161026_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=40)),
                ('orderno', models.CharField(default='', max_length=40)),
                ('amount', models.CharField(default='', max_length=40)),
                ('when', models.CharField(default=datetime.datetime(2016, 10, 27, 17, 42, 58, 46969, tzinfo=utc), max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=40)),
                ('orderno', models.CharField(default='', max_length=40)),
                ('amount', models.CharField(default='', max_length=40)),
                ('when', models.CharField(default=datetime.datetime(2016, 10, 27, 17, 42, 58, 47499, tzinfo=utc), max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 10, 27, 17, 42, 58, 44799, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2016, 10, 27, 17, 42, 58, 45613, tzinfo=utc), max_length=40),
        ),
    ]
