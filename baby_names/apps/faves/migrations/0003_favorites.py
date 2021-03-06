# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161025_2125'),
        ('faves', '0002_auto_20161025_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faves.Frequency')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
