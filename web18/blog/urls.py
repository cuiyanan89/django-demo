from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^register/$','blog.views.register'),
	url(r'^login/$', 'blog.views.login_u'),
	url(r'^index/$','blog.views.index'),
	url(r'^log_out/$','blog.views.log_out'),
)