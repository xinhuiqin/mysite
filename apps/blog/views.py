# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView
from django.conf import settings
from .models import Article, Category, Tag


class IndexView(ListView):
    """
    文章列表
    """
    # 设置使用的模型
    model = Article
    # 设置结果需要渲染的模板
    template_name = 'blog/index.html'
    # 设置上下文对象名，前端模板调用
    context_object_name = 'articles'
    # 设置分页，并指定每页显示的数量
    paginate_by = getattr(settings, 'BASE_PAGINATE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_PAGINATE_ORPHANS', 0)

    # 设置排序方式
    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return '-views', '-update_at', '-id'
        return '-is_top', '-create_at'


class CategoryView(ListView):
    """

    分类列表
    """
    model = Category
    template_name = 'blog/category.html'
