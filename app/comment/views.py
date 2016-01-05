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


def load_more_comment(request):
    post_id = request.POST.get('post_id', False)
    start = request.POST.get('start', False)
    end = request.POST.get('end', False)
    number_comment = request.POST.get('number_comment', False)
    response_data = []
    data_1 = {}
    if int(end) < int(number_comment):
        comments = Comment.objects.filter(post__id=post_id).order_by('-id')[int(start):int(end)]
    else:
        comments = Comment.objects.filter(post__id=post_id).order_by('-id')[int(start):int(number_comment)]

    for i in range(len(comments)):
        comment = load_one_comment(comments[i].id)
        response_data.append(
            render_to_string('comment/comment_post.html', {'comment': comment, 'user': request.user}))
        data_1 = {
            'data': response_data
        }
    return JsonResponse(data_1)


def load_one_comment(id_comment):
    obj = Comment.objects.get(id=id_comment)
    return obj
