from django.conf.urls import url

from app.comment import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^create/post', views.comment_create_post, name='post_like'),
]
