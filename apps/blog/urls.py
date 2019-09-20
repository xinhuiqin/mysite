# -*- coding:utf-8 -*-

from django.urls import path, include
from .views import IndexView, CategoryView, DetailView

app_name = 'blog'
urlpatterns = [
    # 博客首页
    path('', IndexView.as_view(), name='index'),
    # 博客详情页
    path('detail/<int:id>', DetailView.as_view(), name='detail'),
]
