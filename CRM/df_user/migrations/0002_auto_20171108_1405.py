# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tel',
        ),
    ]