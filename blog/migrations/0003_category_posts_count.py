# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-26 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161025_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts_count',
            field=models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u6570\u91cf'),
        ),
    ]
