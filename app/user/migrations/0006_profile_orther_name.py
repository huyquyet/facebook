# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profile_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='orther_name',
            field=models.TextField(default='name'),
        ),
    ]
