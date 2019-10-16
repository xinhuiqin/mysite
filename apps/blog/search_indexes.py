# -*- coding:utf-8 -*-

from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """
    文章搜索索引.
    1.名字必须是model+Index
    2.document=True,表示该字段进行搜索查询的主要字段，该字段建议命名为text.
    3.use_template=True,表示通过数据模板提供text的值。

    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
