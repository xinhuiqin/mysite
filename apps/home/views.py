# -*- coding:utf-8 -*-
from django.shortcuts import render


def index(request):
    """
    首页
    """
    context = {}
    return render(request, 'home/index.html', context)
