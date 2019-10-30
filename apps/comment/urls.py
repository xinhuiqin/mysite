# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('notification/', views.notification, name='notification'),
    path('notification/no-read/', views.notification, {'is_read': 'false'}, name='notification_no_read'),
    path('notification/read/', views.notification, {'is_read': 'True'}, name='notification_read'),
]