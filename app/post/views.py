# Create your views here.
from django.http import JsonResponse

from django.template.loader import render_to_string

from app.activity.models import Activity

from app.post.models import Post


def post_home(request):
    content_post = request.POST.get('content_post', False)
    response_data = {}

    if content_post and request.user:
        post = Post.objects.create(profile__user=request.user, title=content_post)
        post.save()

        #  Create activity
        try:
            activity = Activity.objects.create(profile__user=request.user, type_activity=2, object_id=post.pk,
                                               data=post.title)
            activity.save()
        except Exception as e:
            pass

        html = render_to_string('post/post.html', {'post': post})
        res = {'html': html}
        return JsonResponse(res)
    else:
        response_data['result'] = 'error'
        return JsonResponse(response_data)
