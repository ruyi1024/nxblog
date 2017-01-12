
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^page/(?P<slug>[a-z]+)/$', views.page, name='page'),
    url(r'^category/$', views.category, name='category'),
    url(r'^category/(?P<slug>[a-z]+)/$', views.category_post, name='category'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^search/$', views.search, name='search'),

]