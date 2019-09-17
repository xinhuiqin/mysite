# -*- coding:utf-8 -*-

from django.urls import path, include
from .views import IndexView, CategoryView

app_name = 'blog'
urlpatterns = [
    # 博客首页
    path('', IndexView.as_view(), name='index'),
    # 博客分类页
    path(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
]
