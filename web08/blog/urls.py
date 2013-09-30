from django.conf.urls import patterns, include, url
	

urlpatterns = patterns('',
	
	url(r'^$','blog.views.login'),
	url(r'^login/$','blog.views.login'),
	# url(r'^(?P<name>\w+)/$','blog.views.index',),
	url(r'^regist/$','blog.views.regist'),
	url(r'^success/$','blog.views.success'),
	)