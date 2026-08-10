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
]