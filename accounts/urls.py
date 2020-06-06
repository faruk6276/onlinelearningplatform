from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('activate/<uidb64>/<token>/',views.ActivateAccountView,name='activate'),
    #path('resetpassword/<uidb64>/<token>',views.resetpassconf, name='resetpassconf'),
    #path('resetpass', views.resetpass, name='resetpass'),
    #path('resetdone', views.resetdone, name='resetdone'),
    #path('sendconfresetpass', views.sendconfresetpass, name='sendconfresetpass')
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='resetpassword.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
         template_name='sendconfresetpass.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='resetpasswordconfirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='resetpasswordcomplete.html'), name="password_reset_complete")



]
