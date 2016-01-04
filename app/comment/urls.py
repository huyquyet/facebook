from django.conf.urls import url

from app.comment import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^create/post', views.comment_create, name='comment_create'),
    url(r'^delete/post', views.comment_delete, name='comment_delete'),
    url(r'^edit/post', views.comment_update, name='comment_edit'),
]
