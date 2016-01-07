from django.conf.urls import url

from app.activity import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.activity_user, name='activity_user'),
]
