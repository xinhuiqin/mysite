# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import markdown

# 状态
STATUS = (
    (1, "启用"),
    (0, "禁用"),
)
# 文章图片默认地址
IMG_LINK = '/static/images/blog/article-bg.png'


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='分类名称')
    slug = models.SlugField(unique=True, verbose_name='唯一标识')
    description = models.TextField(max_length=300, default=settings.SITE_DESCRIPTION, verbose_name='分类描述')
    status = models.IntegerField(default=1, choices=STATUS, verbose_name='状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_article_list(self):
        return Article.objects.filter(category=self)


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='标签名称')
    slug = models.SlugField(unique=True, verbose_name='唯一标识')
    description = models.TextField(max_length=300, default=settings.SITE_DESCRIPTION, verbose_name='分类描述')
    status = models.IntegerField(default=1, choices=STATUS, verbose_name='状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})

    def get_article_list(self):
        """返回当前标签下所有发表的文章列表"""
        return Article.objects.filter(tags=self)


class Keyword(models.Model):
    """
    文章关键词
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='文章关键词')
    status = models.IntegerField(default=1, choices=STATUS, verbose_name='状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, verbose_name='文章标签')
    keywords = models.ManyToManyField(Keyword, verbose_name='文章关键词')
    title = models.CharField(max_length=50, verbose_name='文章标题')
    summary = models.TextField(max_length=250, blank=True, default='', verbose_name='文章摘要')
    body = models.TextField(verbose_name='文章内容')
    # ImageField依赖Pillow库
    img_link = models.ImageField(default=IMG_LINK, upload_to='article/%Y%m%d%H%M%S', max_length=255, verbose_name='文章图片')
    views = models.IntegerField(default=0, verbose_name='文章阅读量')
    is_top = models.BooleanField(default=False, verbose_name='是否置顶')
    slug = models.SlugField(unique=True, verbose_name='唯一标识')
    status = models.IntegerField(default=1, choices=STATUS, verbose_name='状态')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_at']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        """
        获取文章唯一路径
        1.blog:detail:blog应用下name为detail的函数
        2.kwargs={'slug': self.slug})：slug的值传给pa
        """
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        """添加markdown"""
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        """更新阅读量"""
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        """获取上一页"""
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        """获取下一页"""
        return Article.objects.filter(id__gt=self.id).order_by('id').first()
