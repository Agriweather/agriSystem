# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20170625_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldlog',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fields.Field'),
        ),
    ]
