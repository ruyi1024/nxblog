#coding=utf-8
from django.db import models
from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Register your models here.
from .models import Category,Post,Page

# Globally disable delete selected
admin.site.disable_action('delete_selected')

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name','slug','status','sort')
    list_display = ('name','slug','status','sort','posts_count','create_time','update_time')
    search_fields = ('name', 'slug',)
    list_editable = ('slug', 'status', 'sort')
admin.site.register(Category,CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category','title','slug','content',)
        }),
        ('Advanced options', {
            'classes': ('collapse'),
            'fields': ('status','description','image')
        }),
    )
    exclude = ('create_time','update_time',)
    list_display = ('title','slug','category_id','status','view_count','create_time','update_time',)
    search_fields = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    actions = ['make_published','make_unpublished']
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



admin.site.register(Post,PostAdmin)


class PageAdmin(admin.ModelAdmin):
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

admin.site.register(Page, PageAdmin)

@receiver(post_save, sender=Post)
def post_after(sender, created, instance, **kwargs):
    category = Category.objects.get(pk=instance.category_id)
    category.posts_count += 1
    category.save()