# -*- coding:utf-8 -*-

from django.urls import path, include
from .views import IndexView

app_name = 'blog'
urlpatterns = [
    # 博客首页
    path('', IndexView.as_view(), name='index'),
]
