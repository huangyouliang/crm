# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20, verbose_name='商品名称')),
                ('gpic', models.ImageField(upload_to='goods', verbose_name='商品照片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='商品价格')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('gunit', models.CharField(default='500g', max_length=20, verbose_name='商品重量')),
                ('gclick', models.IntegerField(verbose_name='点击量')),
                ('gjianjie', models.CharField(max_length=200, verbose_name='简介')),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='详细信息')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
    ]
