#_*_coding:utf-8_*_ 

from django.conf.urls.defaults import patterns, include, url
from blog.models import Product

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^product/create/$', 'blog.views.create_product'),
    url(r'^product/list/$', 'blog.views.list_product'),
    url(r'^product/edit/$', 'blog.views.edit_product'),
    url(r'^product/view/$', 'blog.views.view_product'),
)
