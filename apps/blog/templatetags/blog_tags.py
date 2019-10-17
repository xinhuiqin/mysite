# -*- coding:utf-8 -*-
from django import template
from django.db.models.aggregates import Count
from ..models import Category, Article

register = template.Library()


@register.inclusion_tag('blog/tags/article_list.html')
def load_article_summary(articles):
    """

    文章列表标签模板
    """
    return {'articles': articles}


@register.inclusion_tag('blog/tags/category_list.html')
def get_category_list():
    """

    分类目录标签模板:
    1.统计各分类下文章总数：Count()，接受的参数是需要计数的模型名称。
    """
    categories = Category.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)

    return {'categories': categories}


@register.inclusion_tag('blog/tags/archive_list.html')
def get_archive_list():
    """

    归档目录标签模板
    1.按月度进行归档(dates())
    """
    date_list = Article.objects.dates('create_at', 'month', order='DESC')
    return {'date_list': date_list}


@register.simple_tag
def get_archive_num(year, month):
    """

    归档目录统计总数
    1.统计记录总数：count()
    """
    archive_num = Article.objects.filter(create_at__year=year, create_at__month=month).count()
    return archive_num


@register.inclusion_tag('blog/tags/page.html', takes_context=True)
def load_pages(context):
    """

    分页标签模板
    1.需要访问当前上下文，设置takes_context=True,同时方法第一个参数必须是context
    """
    return context


@register.inclusion_tag('blog/tags/search_box.html', takes_context=True)
def get_search_box(context):
    """
    搜索框
    """
    return context
