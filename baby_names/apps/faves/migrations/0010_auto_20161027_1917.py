# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faves', '0009_merge_20161027_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frequency',
            options={'managed': False},
        ),
    ]