# -*- coding:utf-8 -*-
from django import template
from django.db.models.aggregates import Count
from ..models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/article_list.html')
def load_article_summary(articles):
    """

    返回文章列表模板
    """
    return {'articles': articles}


@register.inclusion_tag('blog/tags/category_list.html')
def get_category_list():
    """

    返回分类列表:
    1.统计各分类下文章总数：Count()，接受的参数是需要计数的模型名称。
    """
    categories = Category.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)
    return {'categories': categories}
