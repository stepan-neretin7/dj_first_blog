# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-16 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180215_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article_for',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
