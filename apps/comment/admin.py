# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import ArticleComment


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    # 设置排序时间
    date_hierarchy = 'create_at'
    list_display = ('id', 'user', 'content', 'article', 'create_at')
