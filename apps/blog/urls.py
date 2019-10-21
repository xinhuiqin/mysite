# -*- coding:utf-8 -*-

from django.urls import path, include
from .views import test_view
from .views import IndexView
from .views import CategoryView
from .views import DetailView
from .views import ArchiveView
from .views import ArticleSearchView

app_name = 'blog'
urlpatterns = [
    # 测试用
    path('test_view/', test_view, name='test_view'),
    # 博客首页
    path('', IndexView.as_view(), name='index'),
    # 博客详情页,将接收到的slug转为slug类型
    path('detail/<slug:slug>/', DetailView.as_view(), name='detail'),
    # 博客分类页
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    # 博客归档页
    path('archive/<int:year>/<int:month>/', ArchiveView.as_view(), name='archive'),
    # 博客文章搜索
    path('search/', ArticleSearchView.as_view(), name='search'),
    path('searchs/', include('haystack.urls')),
]
