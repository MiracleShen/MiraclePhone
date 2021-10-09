
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
class Service(models.Model):
    TYPE = (
        ('Phone', 'Phone'),
        ('PBX', 'PBX'),
        ('Number', 'Number'),
    )

    MUST = (
        ('必选', '必选'),
        ('可选', '可选'),
    )
    UNIT = (
        ('元/月.个', '元/月.个'),
        ('元/月.套', '元/月.套'),
        ('元/月.号', '元/月.号'),
        ('元/月.线', '元/月.线'),
        ('元/分钟', '元/分钟'),
    )
    idx = models.IntegerField(null=True,blank=True, verbose_name='顺序')
    Type = models.CharField(max_length=60,null=True,blank=True, verbose_name='类别',choices=TYPE)
    Name = models.CharField(max_length=20, verbose_name='名称')
    Must = models.CharField(max_length=10,verbose_name='必要性',choices=MUST)
    Price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='价格')
    Unit = models.CharField(max_length=10,verbose_name='单位',choices=UNIT)
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updatedtime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    Memo = models.TextField(null=True,blank=True,verbose_name='备注')
    class Meta:
        verbose_name_plural = '服务价目表'
class Park(models.Model):
    PARK_LEVEL = (
        ('A、物业可办理', 'A、物业可办理'),
        ('B、有客户', 'B、有客户'),
        ('C、4小时开通', 'C、4小时开通'),
        ('D、24小时上门', 'D、24小时开通'),
    )
    PM =(
        ('沈承永','沈承永'),
        ('张浩','张浩'),
    )
    Province = models.CharField(max_length=30,null=True,blank=True, verbose_name='省份')
    City = models.CharField(max_length=30,null=True,blank=True, verbose_name='城市')
    District = models.CharField(max_length=30, null=True, blank=True, verbose_name='区县')
    Town = models.CharField(max_length=30,null=True,blank=True, verbose_name='乡镇')
    Name = models.CharField(max_length=30,null=True,blank=True, verbose_name='园区名称')
    Address = models.CharField(max_length=50,null=True,blank=True,verbose_name='地址')
    Level = models.CharField(max_length=60,null=True,blank=True, verbose_name='类别',choices=PARK_LEVEL)
    Manager = models.CharField(max_length=60,null=True,blank=True, verbose_name='园区经理',choices=PM)
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updatedtime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    Memo = models.TextField(null=True,blank=True,verbose_name='备注')
    class Meta:
        verbose_name_plural = '园区'
