# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_auto_20171108_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ID_num',
            field=models.CharField(default=0, max_length=18, verbose_name='身份证'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='所在城市'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=20, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.CharField(default='', max_length=200, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=True, upload_to='', verbose_name='照片'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default='', max_length=5, verbose_name='性别'),
        ),
    ]