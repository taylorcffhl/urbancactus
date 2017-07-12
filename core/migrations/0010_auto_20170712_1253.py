# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-12 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170711_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productseries',
            name='id',
        ),
        migrations.AddField(
            model_name='productseries',
            name='slug',
            field=models.SlugField(default='', max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]