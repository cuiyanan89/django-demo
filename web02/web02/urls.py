#_*_coding:utf-8_*_
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web02.views.home', name='home'),
    # url(r'^web02/', include('web02.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^ajax/$','blog.views.ajax'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','blog.views.index'),  #提供路由使视图可以处理
    url(r'^json/$', 'blog.views.tjson'),
)
