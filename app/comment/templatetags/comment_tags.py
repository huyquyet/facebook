from django import template

__author__ = 'FRAMGIA\nguyen.huy.quyet'
register = template.Library()


@register.assignment_tag
def  return_comment_of_post(post_id, count):
    pass
