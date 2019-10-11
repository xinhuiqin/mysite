# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article



user_model = settings.AUTH_USER_MODEL


@login_required
@require_POST
def add_comment(request):
    if request.is_ajax() and request.method == 'POST':
        article_id = request.POST.get('article_id')
        article = Article.objects.get(id=article_id)
        print(article_id)