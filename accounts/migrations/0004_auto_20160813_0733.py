# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='email address'),
        ),
    ]
