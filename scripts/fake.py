# -*- coding:utf-8 -*-
import datetime
import getpass
from logging import getLogger
import os
import pathlib
import random
import sys

import django
# 自定义了用户模型，所以使用该方式获取User
from django.contrib.auth import get_user_model
import faker

logger = getLogger('default')
# 实例化Faker
faker = faker.Faker(locale='zh_CN')

# 将项目根目录添加到python的模块搜索路径中
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    # 启动django, 只有启动了Django，才能使用django的，ORM系统
    django.setup()
    from comment.models import ArticleComment
    from comment.models import Notification

    # 清除旧数据
    Notification.objects.all().delete()
    User = get_user_model()
    sender = User.objects.get(id=2)
    receiver = User.objects.get(id=1)

    logger.info('{0} generate fake data  at {1}'.format(getpass.getuser(), datetime.datetime.now()))
    comment = ArticleComment.objects.get(id=13)
    for _ in range(10):
        Notification.objects.create(sender=sender, receiver=receiver, comment=comment, create_at=faker.date_time(),
                                    status=1,
                                    is_read=faker.random_int(0, 1))
    print('Done at {0}'.format(datetime.datetime.now()))
