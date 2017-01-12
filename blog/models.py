#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField
from markdown import markdown

# Create your models here.

class Category(models.Model):
    name = models.CharField(u'名称',max_length=50)
    slug = models.SlugField('标示',max_length=100)
    STATUS = ((1, '启用'), (0, '禁用'))
    status = models.IntegerField('状态',default=0,choices=STATUS)
    sort = models.IntegerField('排序',default=100)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('修改时间',auto_now=True)
    posts_count = models.IntegerField('文章数量',default=0)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __unicode__(self):
        return u"%s" % self.name




class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('文章标题',max_length=100)
    slug = models.SlugField('标示',max_length=100)
    image = models.ImageField('图片',upload_to='post/%Y-%m-%d',null=True,blank=True)
    description = models.CharField('文章描述',max_length=1000,help_text='文章描述可以为空',blank=True)
    content = models.TextField('文章内容',null=True)
    author = models.CharField('作者',max_length=20,blank=True)
    STATUS = ((1, '发布'), (0, '草稿'))
    status = models.IntegerField('状态', default=0, choices=STATUS)
    view_count = models.IntegerField('浏览次数', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __unicode__(self):
        return u"%s" % self.title


class Page(models.Model):
    title = models.CharField('页面标题',max_length=50)
    slug = models.SlugField('标示',max_length=100)
    content = models.TextField('页面内容',null=True)
    author = models.CharField('作者',max_length=20)
    STATUS = ((1, '发布'), (0, '草稿'))
    status = models.IntegerField('状态', default=0, choices=STATUS)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = "页面"
        verbose_name_plural = "页面"

    def __unicode__(self):
        return u"%s" % self.title





