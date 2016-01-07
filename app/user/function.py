from django.contrib.auth.models import User

from app.friend.models import Friend, Waiting, Request, Block
from app.like.function import return_user_like_post
from app.post.models import Post

__author__ = 'FRAMGIA\nguyen.huy.quyet'


def get_post_home(user_id):
    posts = Post.objects.filter(profile__user=User.objects.get(pk=user_id)).order_by('-pk')[0:10]
    for post in posts:
        post.total_like = post.get_total_like()
        post.users_like = return_user_like_post(post.pk)
    return posts


def get_post_timeline(user_id):
    posts = Post.objects.filter(profile__user=User.objects.get(pk=user_id)).order_by('-pk')[0:10]
    for post in posts:
        post.total_like = post.get_total_like()
        post.users_like = return_user_like_post(post.pk)
    return posts


def list_friend_user(user_id):
    list_profile_id = Friend.objects.filter(profile__user=User.objects.get(pk=user_id)).values_list('friend', flat=True)
    list_user = [User.objects.get(profile__id=i) for i in list_profile_id]
    return list_user


def list_user_activity(user_id):
    list_user = list_friend_user(user_id)
    list_user.append(User.objects.get(pk=user_id))
    return list_user


def check_relationship_user(user_id_1, user_id_2):
    if check_friend(user_id_1, user_id_2):
        return 'friend'
    elif check_waiting(user_id_1, user_id_2):
        return 'waiting'
    elif check_request(user_id_1, user_id_2):
        return 'request'
    elif check_block(user_id_1, user_id_2):
        return 'block'
    else:
        return 'none'


def check_friend(user_id_1, user_id_2):
    result = Friend.objects.filter(profile__user__id=user_id_1, friend__user__id=user_id_2).exists()
    return result


def check_waiting(user_id_1, user_id_2):
    result = Waiting.objects.filter(profile__user__id=user_id_1, waiting__user__id=user_id_2).exists()
    return result


def check_request(user_id_1, user_id_2):
    result = Request.objects.filter(profile__user__id=user_id_1, request__user__id=user_id_2).exists()
    return result


def check_block(user_id_1, user_id_2):
    result = Block.objects.filter(profile__user__id=user_id_1, block__user__id=user_id_2).exists()
    result_1 = Block.objects.filter(profile__user__id=user_id_2, block__user__id=user_id_1).exists()
    if result or result_1:
        return True
    else:
        return False
