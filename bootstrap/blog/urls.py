from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	
	url(r'^(?P<name>\w+)/$','blog.views.index',),
	)