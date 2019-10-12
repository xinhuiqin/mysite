# -*- coding:utf-8 -*-

from django.urls import path
from .views import IndexView, CategoryView, DetailView, ArchiveView

app_name = 'blog'
urlpatterns = [
    # 博客首页
    path('', IndexView.as_view(), name='index'),
    # 博客详情页,将接收到的slug转为slug类型
    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    # 博客分类页
    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    # 博客归档页
    path('/archive/', ArchiveView.as_view(), name='archive'),
]
