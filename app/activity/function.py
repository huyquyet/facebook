from datetime import datetime

from django.shortcuts import get_object_or_404

from app.activity.models import Activity, TypeActivity
from app.user.function import list_user_activity
from app.user.models import Profile

__author__ = 'FRAMGIA\nguyen.huy.quyet'


def create_activity(user, activity, object_id, data):
    #  Create activity
    type_activity = return_type_activity(activity)
    if type_activity != 0:
        try:
            activity, create = Activity.objects.get_or_create(profile=Profile.objects.get(user=user),
                                                              type_activity=type_activity, object_id=object_id,
                                                              data=data)
            activity.date = datetime.now()
            activity.save()
        except Exception as e:
            pass
    else:
        return False


def return_type_activity(name):
    try:
        type_activity = get_object_or_404(TypeActivity, name=name)
        return type_activity
    except:
        return 0


def return_activity_user(user_id):
    pass


def return_activity_friend_user(user_id):
    print('abc')
    list_friend = list_user_activity(user_id)
    list_activity = Activity.objects.filter(profile__user__in=list_friend).order_by('-date')
    return list_activity
