#coding=utf-8
from django.db import models
from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget

import xadmin
from xadmin import views
# Register your models here.
from .models import Category,Post,Page


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "Test Widget", "content": "<h3> Welcome to Xadmin! </h3><p>Join Online Group: <br/>QQ Qun : 282936295</p>"},
            {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
            {"type": "list", "model": "app.host", 'params': {
                'o':'-guarantee_date'}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': Page}, {'model':Category}, {'title': "Google", 'url': "http://www.google.com"}]},
            {"type": "addform", "model": Post},
        ]
    ]
xadmin.sites.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.sites.site.register(views.BaseAdminView, BaseSetting)

class CategoryAdmin(object):
    fields = ('name','slug','status','sort')
    list_display = ('name', 'slug', 'status', 'sort', 'posts_count', 'create_time', 'update_time')
    search_fields = ('name', 'slug',)
    list_editable = ('name','slug', 'status', 'sort')
xadmin.site.register(Category, CategoryAdmin)

class PostAdmin(object):
    fields = ('category','title','slug','image','content','status','description')
    exclude = ('create_time','update_time',)
    list_display = ('title','slug','category','status','view_count','create_time','update_time',)
    search_fields = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = "1 文章"
        else:
            message_bit = "%s 文章" % rows_updated
        self.message_user(request, "%s 成功发布." % message_bit)

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status=0)
        if rows_updated == 1:
            message_bit = "1 文章"
        else:
            message_bit = "%s 文章" % rows_updated
        self.message_user(request, "%s 成功下架." % message_bit)

    make_published.short_description = "发布所选的文章"
    make_unpublished.short_description = "下架所选的文章"


xadmin.site.register(Post, PostAdmin)


class PageAdmin(object):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('title','slug','content','status',)
    list_display = ('title','slug','status',)
    search_fields = ('title', 'slug',)
    list_filter = ('status',)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

xadmin.site.register(Page, PageAdmin)
