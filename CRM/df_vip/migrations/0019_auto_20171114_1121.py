# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_vip', '0018_auto_20171114_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.User'),
        ),
    ]
