#coding=utf-8
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template import loader
from .models import Post,Category,Page
# Create your views here.

@require_http_methods(["GET", "POST"])

def index(request):
    posts_list = Post.objects.all().order_by('-create_time')
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)
    posts_hot = Post.objects.all().order_by('-view_count')[:5]
    categorys_list = Category.objects.all().filter(status=1).order_by('sort')
    content = {
        'posts_list':posts_list,
        'paginator':paginator,
        'page':page,
        'posts_hot':posts_hot,
        'categorys_list': categorys_list
    }
    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render(content, request))

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.view_count+=1
    post.save()
    category = Category.objects.get(pk=post.category_id)
    return render(request, 'blog/detail.html', {'post': post,'category':category})

def category(request):
    categorys_list = Category.objects.all().filter(status=1).order_by('sort')
    content = {
        'categorys_list':categorys_list,
    }
    template = loader.get_template('blog/category.html')
    return HttpResponse(template.render(content,request))

def category_post(request,slug):
    category=Category.objects.get(slug=slug)
    posts_list = Post.objects.filter(category_id=category).order_by('-create_time')[:10]
    posts_hot = Post.objects.filter(category_id=category).order_by('-view_count')[:5]
    categorys_list = Category.objects.all().filter(status=1).order_by('sort')
    content = {
        'category':category,
        'posts_list': posts_list,
        'posts_hot': posts_hot,
        'categorys_list': categorys_list
    }
    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render(content, request))

def search(request):
    keyword = request.GET.get('q')
    posts_list = Post.objects.filter(title__icontains=keyword).order_by('-create_time')[:10]
    posts_hot = Post.objects.all().order_by('-view_count')[:5]
    categorys_list = Category.objects.all().filter(status=1).order_by('sort')
    content = {
        'keyword': keyword,
        'posts_list': posts_list,
        'posts_hot': posts_hot,
        'categorys_list': categorys_list
    }
    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render(content, request))

def archive(request):
    posts_list = Post.objects.order_by('-create_time')
    content = {'posts_list': posts_list}
    template = loader.get_template('blog/archive.html')
    return HttpResponse(template.render(content, request))

def page(request,slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'blog/page.html', {'page': page})

