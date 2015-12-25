from django.db import models

# Create your models here.
from django.utils import timezone
from app.user.models import Profile


class Friend(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_friend')
    friend = models.ForeignKey(Profile, related_name='friend_friend')
    date = models.DateTimeField(default=timezone.now)


class Waiting(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_waiting')
    waiting = models.ForeignKey(Profile, related_name='friend_waiting')
    date = models.DateTimeField(default=timezone.now)


class Request(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_request')
    request = models.ForeignKey(Profile, related_name='friend_request')
    date = models.DateTimeField(default=timezone.now)


class Block(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_block')
    block = models.ForeignKey(Profile, related_name='friend_block')
    date = models.DateTimeField(default=timezone.now)
