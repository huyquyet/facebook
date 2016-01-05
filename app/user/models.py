from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone
from facebook import settings


def _path_to_avatar(instance, filename):
    return '{user_id}/{dir_name}/{file_name}'.format(user_id=instance.user.id, dir_name=settings.AVATAR_DIR,
                                                     file_name=filename)


def _path_to_cover(instance, filename):
    return '{user_id}/{dir_name}/{file_name}'.format(user_id=instance.user.id, dir_name=settings.COVER_DIR,
                                                     file_name=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    avatar = models.ImageField(upload_to=_path_to_avatar, max_length=255, default='avatar/default.jpg', blank=False)
    cover = models.ImageField(upload_to=_path_to_cover, max_length=255, default='cover/default.jpg', blank=False)
    address = models.TextField(default='')

    follows = models.ManyToManyField('self', through='Follow', through_fields=('following', 'follower'),
                                     related_name='following', symmetrical=False)

    friends = models.ManyToManyField('self', through='friend.Friend', through_fields=('profile', 'friend'),
                                     related_name='friend', symmetrical=False)

    waitings = models.ManyToManyField('self', through='friend.Waiting', through_fields=('profile', 'waiting'),
                                      related_name='waiting', symmetrical=False)

    requests = models.ManyToManyField('self', through='friend.Request', through_fields=('profile', 'request'),
                                      related_name='request', symmetrical=False)

    blocks = models.ManyToManyField('self', through='friend.Block', through_fields=('profile', 'block'),
                                    related_name='block', symmetrical=False)

    status = models.BooleanField(default=True)


class Follow(models.Model):
    following = models.ForeignKey(Profile, related_name='follower')  # Nguoi theo doi
    follower = models.ForeignKey(Profile, related_name='followee')  # Nguoi dc theo doi
    date = models.DateTimeField(default=timezone.now)
