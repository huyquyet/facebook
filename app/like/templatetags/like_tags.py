from django import template

from app.like.function import return_user_like_comment

__author__ = 'FRAMGIA\nguyen.huy.quyet'
register = template.Library()


@register.assignment_tag
def return_user_like_comment_tags(comment_id):
    users = return_user_like_comment(comment_id)
    return users
