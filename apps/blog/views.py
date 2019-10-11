# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.utils.text import slugify
import markdown
from .models import Article, Category


def pagination_data(paginator, page, is_paginated):
    """
     自定义分页方法
    """
    if not is_paginated:
        # 如果没有分页，则无需显示分页导航条，不用任何分页导航条的数据，因此返回一个空的字典
        return {}

    # 当前页左边连续的页码号，初始值为空
    left = []

    # 当前页右边连续的页码号，初始值为空
    right = []

    # 标示第 1 页页码后是否需要显示省略号
    left_has_more = False

    # 标示最后一页页码前是否需要显示省略号
    right_has_more = False

    # 标示是否需要显示第 1 页的页码号。
    # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
    # 其它情况下第一页的页码是始终需要显示的。
    # 初始值为 False
    first = False

    # 标示是否需要显示最后一页的页码号。
    # 需要此指示变量的理由和上面相同。
    last = False

    # 获得用户当前请求的页码号
    page_number = page.number

    # 获得分页后的总页数
    total_pages = paginator.num_pages

    # 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
    page_range = paginator.page_range

    if page_number == 1:
        # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
        # 此时只要获取当前页右边的连续页码号，
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
        # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
        right = page_range[page_number:page_number + 2]

        # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
        # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
        if right[-1] < total_pages - 1:
            right_has_more = True

        # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
        # 所以需要显示最后一页的页码号，通过 last 来指示
        if right[-1] < total_pages:
            last = True

    elif page_number == total_pages:
        # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
        # 此时只要获取当前页左边的连续页码号。
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
        # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

        # 如果最左边的页码号比第 2 页页码号还大，
        # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
        if left[0] > 2:
            left_has_more = True

        # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
        # 所以需要显示第一页的页码号，通过 first 来指示
        if left[0] > 1:
            first = True
    else:
        # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
        # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        right = page_range[page_number:page_number + 2]

        # 是否需要显示最后一页和最后一页前的省略号
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True

        # 是否需要显示第 1 页和第 1 页后的省略号
        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True

    data = {
        'left': left,
        'right': right,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'first': first,
        'last': last,
    }

    return data


class IndexView(ListView):
    """

    文章列表
    """
    # 设置使用的模型
    model = Article
    # 设置结果需要渲染的模板
    template_name = 'blog/index.html'
    # 设置上下文对象名，前端模板调用
    context_object_name = 'articles'
    # 设置分页，并指定每页显示的数量
    paginate_by = getattr(settings, 'BASE_PAGINATE_BY', None)

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        https://docs.djangoproject.com/en/2.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
        在类视图中，需要传递给模板的字典变量是通过get_context_data()获得的，所以重写该方法。
        """
        # 获取父类生成的传递给模板的字典变量
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的方法进行分页
        pd = pagination_data(paginator, page, is_paginated)

        context.update(pd)

        return context

    # 设置排序方式
    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return '-views', '-update_at', '-id'
        return '-is_top', '-create_at'


class CategoryView(ListView):
    """

    分类列表
    """
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGINATE_BY', None)

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        https://docs.djangoproject.com/en/2.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
        在类视图中，需要传递给模板的字典变量是通过get_context_data()获得的，所以重写该方法。
        """
        # 获取父类生成的传递给模板的字典变量
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的方法进行分页
        pd = pagination_data(paginator, page, is_paginated)

        context.update(pd)

        return context

    def get_queryset(self):
        """
        因为要根据category进行查询，所以重写get_query()方法。
        """
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        qs = super(CategoryView, self).get_queryset()
        return qs.filter(category=self.category)

class ArchivesView(ListView):
    model = Article


class DetailView(DetailView):
    """

    详情页
    """
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    #  重写get_object()方法
    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        obj = super(DetailView, self).get_object(queryset=None)
        obj.body = markdown.markdown(obj.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
        # obj.body = md.convert(obj.body)
        return obj


