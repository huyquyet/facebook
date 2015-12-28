from django.conf.urls import url

from app.post import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^/create_post_home$', views.post_home, name='post_home'),

]
