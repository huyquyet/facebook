# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
