# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-16 03:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0137_auto_20170207_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='creater_enrollment',
            new_name='creator_enrollment',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='participation_checkintime',
            new_name='participation_checkin_time',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='participation_form',
            new_name='participation_template',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='participation_date',
            new_name='participation_time',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='user_email',
            new_name='profile_email',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='user_image',
            new_name='profile_image',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='user_introduction',
            new_name='profile_introduction',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='user_name',
            new_name='profile_name',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='user_phone',
            new_name='profile_phone',
        ),
        migrations.AddField(
            model_name='tournament',
            name='confirm',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_endtime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_goal',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_info',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_notice',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_starttime',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='funding_time',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='participation_fee_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='profile_email_question',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='profile_name_question',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='promise_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='reward_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='streaming_site',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_game_etc',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='funding',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 16, 3, 20, 53, 296096, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='fundingdummy',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 16, 3, 20, 53, 294146, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='making',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 16, 3, 20, 53, 296781, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='participation',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 16, 3, 20, 53, 301652, tzinfo=utc), max_length=40),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='promise',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='reward',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='streaming_url',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='video',
            name='when',
            field=models.CharField(default=datetime.datetime(2017, 2, 16, 3, 20, 53, 300890, tzinfo=utc), max_length=40),
        ),
    ]
