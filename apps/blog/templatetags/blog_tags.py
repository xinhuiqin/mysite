# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('blog/tags/article_list.html')
def load_article_summary(articles):
    """

    返回文章列表模板
    """
    return {'articles': articles}
