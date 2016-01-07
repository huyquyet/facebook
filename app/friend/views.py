# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string

from app.friend.models import Request, Waiting, Friend
from app.user.models import Profile


def friend_add(request):
    user_id = request.POST.get('user_id', False)
    response_data = {}

    if user_id and request.user:
        request_user = Request.objects.create(profile=Profile.objects.get(user__id=request.user.pk),
                                              request=Profile.objects.get(user__id=user_id))
        request_user.save()

        waiting_user = Waiting.objects.create(profile=Profile.objects.get(user__id=user_id),
                                              waiting=Profile.objects.get(user__id=request.user.pk))
        waiting_user.save()

        html = render_to_string('friend/friend_status_home/btn_request.html',
                                {'user_home': User.objects.get(pk=user_id)})
        response_data = {'html': html, 'result': True}
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def friend_cancel_request(request):
    user_id = request.POST.get('user_id', False)
    response_data = {}

    if user_id and request.user:
        cancel_request = Request.objects.get(profile=Profile.objects.get(user__id=request.user.pk),
                                             request=Profile.objects.get(user__id=user_id))
        cancel_request.delete()

        delete_waiting = Waiting.objects.get(profile=Profile.objects.get(user__id=user_id),
                                             waiting=Profile.objects.get(user__id=request.user.pk))
        delete_waiting.delete()

        html = render_to_string('friend/friend_status_home/btn_none.html',
                                {'user_home': User.objects.get(pk=user_id)})
        response_data = {'html': html, 'result': True}
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def friend_not_now(request):
    user_id = request.POST.get('user_id', False)
    response_data = {}

    if user_id and request.user:
        delete_waiting = Waiting.objects.get(profile=Profile.objects.get(user__id=request.user.pk),
                                             waiting=Profile.objects.get(user__id=user_id))
        delete_waiting.delete()

        delete_request = Request.objects.get(profile=Profile.objects.get(user__id=user_id),
                                             request=Profile.objects.get(user__id=request.user.pk))
        delete_request.delete()

        html = render_to_string('friend/friend_status_home/btn_none.html',
                                {'user_home': User.objects.get(pk=user_id)})
        response_data = {'html': html, 'result': True}
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def friend_accept(request):
    user_id = request.POST.get('user_id', False)
    response_data = {}

    if user_id and request.user:
        """
        Add friend 2 user
        """
        accept = Friend.objects.create(profile=Profile.objects.get(user__id=user_id),
                                       friend=Profile.objects.get(user__id=request.user.pk))
        accept.save()

        accept = Friend.objects.create(profile=Profile.objects.get(user__id=request.user.pk),
                                       friend=Profile.objects.get(user__id=user_id))
        accept.save()

        """
        Remove data in Request and Waiting
        """
        delete_waiting = Waiting.objects.get(profile=Profile.objects.get(user__id=request.user.pk),
                                             waiting=Profile.objects.get(user__id=user_id))
        delete_waiting.delete()

        delete_request = Request.objects.get(profile=Profile.objects.get(user__id=user_id),
                                             request=Profile.objects.get(user__id=request.user.pk))
        delete_request.delete()

        html = render_to_string('friend/friend_status_home/btn_friend.html',
                                {'user_home': User.objects.get(pk=user_id)})
        response_data = {'html': html, 'result': True}
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)


def friend_remove(request):
    user_id = request.POST.get('user_id', False)
    response_data = {}

    if user_id and request.user:
        remove = Friend.objects.get(profile=Profile.objects.get(user__id=user_id),
                                    friend=Profile.objects.get(user__id=request.user.pk))
        remove.delete()

        remove = Friend.objects.get(profile=Profile.objects.get(user__id=request.user.pk),
                                    friend=Profile.objects.get(user__id=user_id))
        remove.delete()

        html = render_to_string('friend/friend_status_home/btn_none.html',
                                {'user_home': User.objects.get(pk=user_id)})
        response_data = {'html': html, 'result': True}
        return JsonResponse(response_data)
    else:
        response_data['result'] = False
        return JsonResponse(response_data)
