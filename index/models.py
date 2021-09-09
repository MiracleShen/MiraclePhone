
# _*_ coding:utf-8 _*_
from django.db import models


# Create your models here.
class News(models.Model):
    Catagory = models.CharField(max_length=60, verbose_name='类别')
    Title = models.CharField(max_length=20, verbose_name='标题')
    Content = models.TextField(null=True, verbose_name='内容')
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updatedtime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = '新闻'
