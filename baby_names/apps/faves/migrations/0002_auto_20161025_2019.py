# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faves', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='djangomigrations',
            options={'managed': True},
        ),
    ]