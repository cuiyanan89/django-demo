from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'blog.views.index'),
	url(r'^index/$', 'blog.views.index'),
	url(r'^menu/(?P<id>\d+)/$', 'blog.views.menu'),
	url(r'^register/$','blog.views.register'),
	url(r'^login/$','blog.views.login'),
)