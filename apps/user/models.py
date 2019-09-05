# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class USER(AbstractUser):
    """用户

    """
    link = models.URLField(verbose_name='个人网址')

    class Meta:
        db_table = 'user'
        ordering = ['-id']
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username