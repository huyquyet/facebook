from django.db import models

# Create your models here.
from django.utils import timezone
from app.comment.models import Comment
from app.post.models import Post
from app.user.models import Profile


class LikePost(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_likepost')
    post = models.ForeignKey(Post, related_name='post_likepost')
    date = models.DateTimeField(default=timezone.now)


class LikeComment(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_likecomment')
    comment = models.ForeignKey(Comment, related_name='post_likecomment')
    date = models.DateTimeField(default=timezone.now)
