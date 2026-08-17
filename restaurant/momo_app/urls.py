from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('',index, name='index'),
    path('about/', about, name='about'),
    path('services/', services,name='services'),
    path('menu/',menu, name='menu'),
    path('contact/',contact, name='contact'),
    path('testemonials/',testemonial, name='testemonials'),
    path('terms/',term, name='terms'),

    #--------------auth part--------------------------
    path('login/',login_part,name='login_part'),
    path('register/',register,name='register'),
    path('logout/',log_out,name='log_out'),
    path('password_change/',pass_change,name='password_change'),
    # ................forget password............
    path('password_reset/', auth_views.PasswordResetView.as_view( template_name="auth/password_reset.html", html_email_template_name="auth/mail.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="auth/set-password.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view( template_name="auth/password_reset_complete.html"), name='password_reset_complete'),
]
