# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app.activity.function import create_activity
from app.like.function import return_total_like_post
from app.like.models import LikePost
from app.post.models import Post
from app.user.models import Profile


def post_like(request):
    post_id = request.POST.get('post_id', False)
    reponse_data = {}

    if post_id and request.user:
        like, create = LikePost.objects.get_or_create(profile=Profile.objects.get(user=request.user),
                                                      post=Post.objects.get(pk=post_id))
        like.save()
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
    reponse_data = {}

    if post_id and request.user:
        like = get_object_or_404(LikePost, profile=Profile.objects.get(user=request.user),
                                 post=Post.objects.get(pk=post_id))
        like.delete()
        reponse_data['result'] = True
        reponse_data['total_like_post'] = return_total_like_post(post_id)
        return JsonResponse(reponse_data)
    else:
        reponse_data['result'] = False
        return JsonResponse(reponse_data)
