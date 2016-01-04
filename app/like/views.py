# Create your views here.
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app.activity.function import create_activity
from app.comment.models import Comment
from app.like.function import return_total_like_post, return_total_like_comment
from app.like.models import LikePost, LikeComment
from app.post.models import Post
from app.user.models import Profile


def post_like(request):
    post_id = request.POST.get('post_id', False)
    reponse_data = {}

    if post_id and request.user:
        post = Post.objects.get(pk=post_id)
        like, create = LikePost.objects.get_or_create(profile=Profile.objects.get(user=request.user), post=post)
        like.save()

        # Update time when post have a activity
        post.date_activity = datetime.now()
        post.save()

        #  Create activity
        create_activity(request.user, 'like_post', like.post.pk, 'like status')
        reponse_data['result'] = True
        reponse_data['total_like_post'] = return_total_like_post(post_id)
        return JsonResponse(reponse_data)
    else:
        reponse_data['result'] = False
        return JsonResponse(reponse_data)


def post_unlike(request):
    post_id = request.POST.get('post_id', False)
    response_data = {}

    if post_id and request.user:
        like = get_object_or_404(LikePost, profile=Profile.objects.get(user=request.user),
                                 post=Post.objects.get(pk=post_id))
        like.delete()
        response_data['result'] = True
        response_data['total_like_post'] = return_total_like_post(post_id)
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def comment_like(request):
    comment_id = request.POST.get('comment_id', False)
    response_data = {}

    if comment_id and request.user:
        comment = Comment.objects.get(pk=comment_id)
        like, create = LikeComment.objects.get_or_create(profile=Profile.objects.get(user=request.user),
                                                         comment=comment)
        like.save()

        # Update time when post have a activity
        comment.date_activity = datetime.now()

        #  Create activity
        create_activity(request.user, 'like_comment', like.comment.pk, 'like comment')

        response_data['result'] = True
        response_data['total_like_comment'] = return_total_like_comment(comment_id)
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def comment_unlike(request):
    comment_id = request.POST.get('comment_id', False)
    reponse_data = {}

    if comment_id and request.user:
        comment = Comment.objects.get(pk=comment_id)
        like = get_object_or_404(LikeComment, profile=Profile.objects.get(user=request.user), comment=comment)
        like.delete()

        reponse_data['result'] = True
        reponse_data['total_like_post'] = return_total_like_post(comment_id)
        return JsonResponse(reponse_data)
    else:
        reponse_data['result'] = False
        return JsonResponse(reponse_data)
