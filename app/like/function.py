from django.shortcuts import get_object_or_404

from app.like.models import LikePost, LikeComment
from app.post.models import Post
from app.user.models import Profile

__author__ = 'FRAMGIA\nguyen.huy.quyet'


def return_user_like_post(post_id):
    profiles = LikePost.objects.filter(post__id=post_id).values_list('profile', flat=True)
    users = []
    for profile in profiles:
        user = Profile.objects.get(pk=profile).user
        users.append(user)
    return users


def return_total_like_post(post_id):
    post = get_object_or_404(Post, pk=post_id)
    return post.get_total_like()


def return_user_like_comment(comment_id):
    profiles = LikeComment.objects.filter(comment__id=comment_id).values_list('profile', flat=True)
    users = []
    for profile in profiles:
        user = Profile.objects.get(pk=profile).user
        users.append(user)
    return users
