# -*- coding:utf-8 -*-
from django.contrib import admin

from .models import ArticleComment
from .models import Notification


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    # 设置排序时间
    date_hierarchy = 'create_at'
    list_display = ('id', 'user', 'content', 'article', 'create_at')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'is_read', 'create_at')
