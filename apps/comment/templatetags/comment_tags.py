# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('comment/tags/comment_list.html', takes_context=True)
def get_comment_list(context, article):
    """

     评论列表模板.
     1.article_comments为ArticleComments类中外键article的related_name
    """
    return article.article_comments.filter(parent=None)
