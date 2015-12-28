from django.conf.urls import url

from app.user import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^/(?P<username>[\w-]+)$', views.HomeView, name='home'),
    url(r'^/login$', views.UserLoginView, name='login'),
    url(r'^/logout$', views.UserLogoutView, name='user_logout'),
    url(r'^/register$', views.UserRegisterView, name='user_register'),
    url(r'^/(?P<username>[\w-]+)/edit$', views.UserEditProfileView, name='user_edit_profile'),
    url(r'^/(?P<username>[\w-]+)/change_pass$', views.UserChangePassView, name='user_change_pass'),
]
