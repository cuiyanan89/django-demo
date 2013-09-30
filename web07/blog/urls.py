from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^post/$','blog.views.post'),
	url(r'^hello/$', 'blog.views.hello'),
)
