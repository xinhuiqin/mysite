# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from . import handlers
# 不能写成from apps.blog.models import Article
from .models import ArticleComment


user_model = settings.AUTH_USER_MODEL


@login_required
@require_POST
def add_comment(request):
    cmt = {}
    ret = {
        'code': 1,
        'msg': '评论成功',
        'cmt': cmt,
    }
    if request.is_ajax():
        data = request.POST
        user = request.user
        article_id = data.get('article_id')
        content = data.get('content')
        reply_to = data.get('reply_to')
        if not reply_to:
            # 如果不是回复别人
            article_cmt = ArticleComment(user=user, article_id=article_id, content=content, reply_to=None, parent=None)
        else:
            pass
        article_cmt.save()
        cmt['user'] = article_cmt.user.username
        cmt['create_at'] = article_cmt.create_at.strftime('%Y-%m-%d %H:%M:%S')
        cmt['content'] = article_cmt.content

    return HttpResponse(json.dumps(ret))


@login_required
def notification(request, is_read=None):
    context = {
        'is_read': is_read,
    }
    return render(request, 'comment/notification.html', context=context)
