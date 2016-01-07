from django.conf.urls import url

from app.friend import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^friend/add$', views.friend_add, name='friend_add'),
    url(r'^friend/cancel_request$', views.friend_cancel_request, name='friend_cancel_request'),
    url(r'^friend/friend_not_now$', views.friend_not_now, name='friend_not_now'),
    url(r'^friend/friend_accept$', views.friend_accept, name='friend_accept'),
    url(r'^friend/friend_remove', views.friend_remove, name='friend_remove'),
]
