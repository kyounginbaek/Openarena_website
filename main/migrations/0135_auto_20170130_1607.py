# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-30 07:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0134_auto_20170129_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundingdummy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament_id', models.CharField(default='', max_length=20)),
                ('tournament_name', models.CharField(default='', max_length=40)),
                ('username', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=40)),
                ('amount', models.IntegerField(default=0)),
                ('reward', models.CharField(default='-', max_length=100)),
                ('comment', models.TextField(default='-')),
                ('orderno', models.CharField(default='-', max_length=40)),
                ('when', models.CharField(default=datetime.datetime(2017, 1, 30, 7, 7, 13, 749089, tzinfo=utc), max_length=40)),
                ('thanks', models.CharField(default='-', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 30, 7, 7, 13, 751160, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 30, 7, 7, 13, 751729, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 30, 7, 7, 13, 755141, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 1, 30, 7, 7, 13, 754404, tzinfo=utc), max_length=40),
        ),
    ]
