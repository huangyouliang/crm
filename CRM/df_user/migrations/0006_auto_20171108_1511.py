# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0005_auto_20171108_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ID_num',
            field=models.CharField(default='', max_length=18, verbose_name='身份证'),
        ),
    ]
