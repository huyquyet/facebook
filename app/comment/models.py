from django.db import models

# Create your models here.

from django.utils import timezone
from app.post.models import Post
from app.user.models import Profile


class Comment(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_comment')
    post = models.ForeignKey(Post, related_name='post_comment')
    title = models.TextField()
    date = models.DateTimeField(default=timezone.now)