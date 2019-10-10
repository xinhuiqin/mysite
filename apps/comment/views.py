# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

user_model = settings.AUTH_USER_MODEL

@login_required
@require_POST
def add_comment(request):
    print(1111111)
    if request.is_ajax() and request.method == 'POST':
        print(request.user)
