from django.conf.urls import url

from app.like import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^post/like', views.post_like, name='post_like'),
    url(r'^post/unlike', views.post_unlike, name='post_unlike'),
]
