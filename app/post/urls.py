from django.conf.urls import url

from app.post import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^create_post_home$', views.create_post_home, name='create_post_home'),

]
