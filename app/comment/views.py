# Create your views here.
from django.http import JsonResponse
from app.activity.function import create_activity
from app.comment.models import Comment
from app.post.models import Post
from app.user.models import Profile


def comment_create_post(request):
    post_id = request.POST.get('post_id', False)
    content_comment = request.POST.get('content_comment', False)
    reponse_data = {}
    if post_id and request.user:
        comment = Comment.objects.create(post=Post.objects.get(pk=post_id),
                                         profile=Profile.objects.get(user=request.user))
        comment.title = content_comment
        comment.save()
        #  Create activity
        create_activity(request.user, 'comment_post', comment.post.pk, comment.title)
        reponse_data['result'] = True
        return JsonResponse(reponse_data)
    else:
        reponse_data['result'] = False
        return JsonResponse(reponse_data)
