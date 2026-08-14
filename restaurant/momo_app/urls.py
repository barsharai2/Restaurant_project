from django.contrib import admin
from django.urls import path
from .views import *

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
    path('password_change/',pass_change,name='password_change')
]
