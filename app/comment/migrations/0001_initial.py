# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('user', '0004_profile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='post.Post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_comment', to='user.Profile')),
            ],
        ),
    ]
