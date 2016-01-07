# Create your views here.
import json

from django.http import JsonResponse

from app.activity.function import return_activity_friend_user


def activity_user(request):
    response_data = {}
    activities_r = []
    list_activity = return_activity_friend_user(request.user.pk)
    for i in list_activity:
        activities_r.append(json.dumps(i.pk))
    response_data['data'] = activities_r
    # response_data['data'] = json.dumps(list_activity.__dict__)
    return JsonResponse(response_data)
