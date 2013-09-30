from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^authors/$','blog.views.authors'),
	url(r'^books/$','blog.views.books'),
	url(r'^authors/(?P<name>\w+)/$','blog.views.author'),
	url(r'^books/(?P<name>\w+)/$','blog.views.book'),
	)