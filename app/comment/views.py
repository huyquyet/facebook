# Create your views here.
from datetime import datetime

from django.http import JsonResponse
from django.template.loader import render_to_string

from app.activity.function import create_activity
from app.comment.models import Comment
from app.post.models import Post
from app.user.models import Profile


def comment_create(request):
    post_id = request.POST.get('post_id', False)
    content_comment = request.POST.get('content_comment', False)
    response_data = {}

    if post_id and request.user:
        comment = Comment.objects.create(post=Post.objects.get(pk=post_id),
                                         profile=Profile.objects.get(user=request.user))
        comment.title = content_comment
        comment.date = datetime.now()
        comment.save()
        #  Create activity
        create_activity(request.user, 'comment_post', comment.post.pk, comment.title)

        html = render_to_string('comment/comment_post.html', {'comment': comment, 'user': request.user})
        res = {'html': html}
        return JsonResponse(res)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def comment_delete(request):
    comment_id = request.POST.get('comment_id', False)
    response_data = {}

    if comment_id and request.user:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()

        response_data['result'] = True
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def comment_update(request):
    content_comment = request.POST.get('content_comment', False)
    comment_id = request.POST.get('comment_id', False)
    response_data = {}

    if comment_id and content_comment and request.user:
        comment = Comment.objects.get(pk=comment_id)
        comment.title = content_comment
        comment.save()

        response_data['result'] = True
        response_data['data'] = comment.title
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)
