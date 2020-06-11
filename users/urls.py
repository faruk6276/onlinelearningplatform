from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile', views.user_profile_view, name='profile'),
    path('logout', views.logout_view, name='logout')

]
