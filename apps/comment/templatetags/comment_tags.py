# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('comment/tags/comment_list.html', takes_context=True)
def get_comment_list(context, article):
    """

     评论列表模板.
     * 传递一篇文章，然后根据该文章加载评论。
     * article_comments为ArticleComments类中外键article的related_name。
    """
    comment_list = article.article_comments.filter(parent=None)
    return {'comment_list': comment_list}
