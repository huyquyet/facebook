from django.db import models

# Create your models here.
from django.utils import timezone
from app.user.models import Profile

"""
Data TypeActivity
1:  add_friend
2:  write_post
3:  like_post
4:  comment_post
5:  like_comment

"""


class TypeActivity(models.Model):
    name = models.CharField(max_length=255)


class Activity(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_activity')
    type_activity = models.ForeignKey(TypeActivity)
    object_id = models.IntegerField()
    data = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
