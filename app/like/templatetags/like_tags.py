from django import template

from app.like.function import return_user_like_comment, return_count_like_comment

__author__ = 'FRAMGIA\nguyen.huy.quyet'
register = template.Library()


@register.assignment_tag
def return_user_like_comment_tags(comment_id):
    users = return_user_like_comment(comment_id)
    return users

@register.assignment_tag
def return_comment_like_comment_tags(comment_id):
    like = return_count_like_comment(comment_id)
    return like
