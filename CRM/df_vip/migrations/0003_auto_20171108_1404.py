# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_vip', '0002_vip_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_user',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.user'),
        ),
    ]