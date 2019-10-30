# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models


class Comment(models.Model):
    """

    评论基类
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='评论人')
    content = models.TextField(verbose_name='评论内容')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='%(class)s_child_comments',
                               on_delete=models.CASCADE, verbose_name='父评论')
    reply_to = models.ForeignKey('self', blank=True, null=True, related_name='%(class)s_reply_comments',
                                 on_delete=models.CASCADE, verbose_name='被回复的评论')
    create_at = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)

    class Meta:
        # 设置abstract = True，表示只用于继承，不生成数据库表
        abstract = True

    def __str__(self):
        return self.content[:20]


class ArticleComment(Comment):
    """

    文章评论
    """
    article = models.ForeignKey('blog.Article', related_name='article_comments', on_delete=models.CASCADE,
                                verbose_name='文章')

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class Notification(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notif_sender',
                               verbose_name='发送者')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name='notif_receiver', verbose_name='接收者')
    comment = models.ForeignKey(ArticleComment, on_delete=models.CASCADE, related_name='notif_comment',
                                verbose_name='所属评论')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_read = models.IntegerField(default=0, verbose_name='是否已读')

    class Meta:
        verbose_name = '消息通知'
        verbose_name_plural = verbose_name
        ordering = ['-create_at']

    def __str__(self):
        return '{0}评论了你的文章{1}'.format(self.sender, self.comment)

    def mark_read(self):
        self.is_read = 1
        self.save(update_fields=['is_read'])
