# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('comment/tags/comment_form.html', takes_context=True)
def get_comment_form(context):
    """

     评论表单模板.
    """
    return context


@register.inclusion_tag('comment/tags/comment_list.html', takes_context=True)
def get_comment_list(context, article):
    """

     评论列表模板.
     * 传递一篇文章，然后根据该文章加载评论。
     * article_comments为ArticleComments类中外键article的related_name。
    """
    comment_list = article.article_comments.filter(parent=None)
    return {'comment_list': comment_list}


@register.simple_tag
def get_notifications(user, is_read=None):
    """
    评论通知。
    :param user: 用户
    :param is_read: 是否已读
    :return: 消息列表
    """
    if is_read == 'True':
        notifications = user.notif_receiver.filter(is_read=1)
    elif is_read == 'False':
        notifications = user.notif_receiver.filter(is_read=0)
    else:
        notifications = user.notif_receiver.all()
    return notifications


@register.simple_tag
def notifications_count(user, is_read=None):
    """
       消息数量统计
       :param user: 用户
       :param is_read: 是否已读
       :return: 消息数量
       """
    if is_read == 'True':
        notifications_count = user.notif_receiver.filter(is_read=1).count()
    elif is_read == 'False':
        notifications_count = user.notif_receiver.filter(is_read=1).count()
    else:
        notifications_count = user.notif_receiver.all.count()
    return notifications_count
