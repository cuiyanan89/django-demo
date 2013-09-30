from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^register/$','blog.views.register'),
	url(r'^login/$','blog.views.login'),
)
