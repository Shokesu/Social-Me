# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userIdFB',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
