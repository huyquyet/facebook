# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20151225_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='block_friends',
            new_name='blocks',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='request_friends',
            new_name='requests',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='waiting_friends',
            new_name='waitings',
        ),
    ]
