from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
		url(r'^index/$','blog.views.index'),
		url(r'^post/$', 'blog.views.post'),
		url(r'^post_cont/(?P<id>\d+)/$','blog.views.post_cont'),
		url(r'^post_change/(?P<id>\d+)/$','blog.views.post_change'),
		url(r'^post_del/(?P<id>\d+)/$','blog.views.post_del'),
	)