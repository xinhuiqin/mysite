# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Category, Tag, Keyword, Article

# Django admin参考资料：https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

# 自定义管理站点的名称和URL标题
admin.site.site_header = 'Sweeneys官方网站管理后台'
admin.site.site_title = 'Sweeneys官方网站管理后台'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #  设置文章筛选的条件
    date_hierarchy = 'create_at'

    exclude = ('views',)

    # 设置需要显示的内容：在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_at', 'update_at', 'is_top')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 设置过滤器
    list_filter = ('create_at', 'category', 'is_top')

    # 设置每页显示的数量，默认是100
    list_per_page = 50

    # 给多选增加一个左右添加的框
    filter_horizontal = ('tags', 'keywords')

    # 设置用户权限，只能看到自己编辑的文章(重写get_queryset方法)
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
