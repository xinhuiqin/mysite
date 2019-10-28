# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    """
    首页
    """
    context = {}
    return render(request, 'home/index.html', context)


def page_not_found(request, exception):
    """
    404页面
    """
    res = render_to_response('404.html', {})
    res.status_code = 404
    return res
