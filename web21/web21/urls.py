#_*_coding:utf-8_*_
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web21.views.home', name='home'),
    # url(r'^web21/', include('web21.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/',include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'blog.views.index'),
    url(r'^login/$', 'blog.views.login_user'),
    url(r'^logout/$', 'blog.views.logout_user'),
    url(r'^register/$', 'blog.views.register'),
    url(r'^post/(?P<id>\d+)/$', 'blog.views.post'),

)
