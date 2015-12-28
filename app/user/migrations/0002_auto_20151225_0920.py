# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilefriend',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='profilefriend',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='block_friends',
            field=models.ManyToManyField(related_name='block', through='friend.Block', to='user.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='request_friends',
            field=models.ManyToManyField(related_name='request', through='friend.Request', to='user.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_friends',
            field=models.ManyToManyField(related_name='waiting', through='friend.Waiting', to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='friend', through='friend.Friend', to='user.Profile'),
        ),
        migrations.DeleteModel(
            name='ProfileFriend',
        ),
    ]