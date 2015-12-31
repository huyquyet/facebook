# Create your views here.
from django.http import JsonResponse
from django.template.loader import render_to_string

from app.activity.function import create_activity
from app.post.models import Post
from app.user.models import Profile


def create_post_home(request):
    content_post = request.POST.get('content_post', False)
    user_home_id = request.POST.get('user_home_id', False)
    response_data = {}

    if content_post and request.user:
        post = Post.objects.create(profile=Profile.objects.get(user__id=user_home_id),
                                   profile_create=Profile.objects.get(user=request.user), title=content_post)
        post.save()

        try:
            #  Create activity
            create_activity(request.user, 'write_post', post.pk, post.title)
        except:
            pass
        html = render_to_string('post/post.html', {'post': post, 'user': request.user})
        res = {'html': html, 'id_new_post': post.pk}
        return JsonResponse(res)
    else:
        response_data['result'] = 'error'
        return JsonResponse(response_data)
