# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-11 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='content',
            new_name='full_content',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='introduction',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='partners',
            field=models.ManyToManyField(to='core.Partner'),
        ),
    ]