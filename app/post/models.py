from django.db import models


# Create your models here.
from django.utils import timezone
from app.user.models import Profile
from facebook import settings


def _path_to_timeline(instance, filename):
    return '{user_id}/{dir_name}/{file_name}'.format(user_id=instance.user.id, dir_name=settings.TIMELINE,
                                                     file_name=filename)


class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name='post')
    title = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class PostImage(Post):
    image = models.ImageField(upload_to=_path_to_timeline, max_length=255)
