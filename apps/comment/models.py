# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings


class Comment(models.Model):
    """

    评论基类
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='评论人')
    content = models.TextField(verbose_name='评论内容')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='%(class)s_child_comments',
                               on_delete=models.CASCADE, verbose_name='父评论')
    reply_to = models.ForeignKey('self', blank=True, null=True, related_name='%(class)s_reply_comments',
                                 on_delete=models.CASCADE, verbose_name='回复')
    create_at = models.DateTimeField(verbose_name='评论时间')

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
        ordering = ['create_at']
