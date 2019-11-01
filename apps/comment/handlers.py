# -*- coding: utf-8 -*-
# post_save信号：在模型save()方法之后调用
from django.db.models.signals import post_save
from .models import ArticleComment, Notification


def notify_handler(sender, instance, created, **kwargs):
    the_article = instance.article
    sender = instance.user
    # 判断是否是第一次生成评论，后续修改评论不会再次激活信号
    if created:
        if instance.reply_to:
            '''如果评论是一个回复评论，则同时通知给文章作者和回复的评论人，如果2者相等，则只通知一次'''
            if the_article.author == instance.reply_to.author:
                receiver = instance.reply_to.author
                if sender != receiver:
                    new_notify = Notification(sender=sender, receiver=receiver, comment=instance)
                    new_notify.save()
            else:
                receiver1 = the_article.author
                if sender != receiver1:
                    new1 = Notification(sender=sender, receiver=receiver1, comment=instance)
                    new1.save()
                receiver2 = instance.reply_to.author
                if sender != receiver2:
                    new2 = Notification(sender=sender, receiver=receiver2, comment=instance)
                    new2.save()
        else:
            '''如果评论是一个一级评论而不是回复其他评论并且不是作者自评，则直接通知给文章作者'''
            receiver = the_article.author
            if sender != receiver:
                new_notify = Notification(sender=sender, receiver=receiver, comment=instance)
                new_notify.save()


# 信号和接收者函数绑定
post_save.connect(notify_handler, sender=ArticleComment)
