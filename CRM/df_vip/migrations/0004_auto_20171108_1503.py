# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_vip', '0003_auto_20171108_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vip_user',
            name='name',
        ),
        migrations.DeleteModel(
            name='vip_user',
        ),
    ]
