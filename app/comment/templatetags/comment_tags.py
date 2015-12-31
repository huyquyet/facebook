from django import template

from app.comment.models import Comment

__author__ = 'FRAMGIA\nguyen.huy.quyet'
register = template.Library()


@register.assignment_tag
def return_comment_of_post_tags(post_id, count):
    count_comment = return_number_comment_of_post(post_id)
    if count < count_comment:
        comment = Comment.objects.filter(post__id=post_id)[count_comment - count:count_comment]
        return comment
    else:
        comment = Comment.objects.filter(post__id=post_id)
        return comment


def return_number_comment_of_post(post_id):
    count = Comment.objects.filter(post__id=post_id).count()
    return count
