from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$','blog.views.index'),
	url(r'^index/$', 'blog.views.index'),
	url(r'^nav/$','blog.views.disp_nav'),
	url(r'^nav/(?P<id>\d+)/$','blog.views.disp_nav'),
	url(r'^post/(?P<id>\d+)/$','blog.views.post'),
	)
