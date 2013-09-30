from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web20.views.home', name='home'),
    # url(r'^web20/', include('web20.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'blog.views.register'),
    url(r'^login/$','blog.views.login_user'),
    url(r'^index/$','blog.views.index'),
    url(r'^post/(?P<id>\d+)/$','blog.views.post'),
    url(r'^logout/$','blog.views.logout_user'),
)
