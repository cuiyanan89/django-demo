from django.conf.urls import patterns, include, url
from blog.feeds import RSSFeed
from blog.sitemap import BlogSitemap

urlpatterns = patterns('',
	
	url(r'^$','blog.views.index'),
	url(r'^index/$','blog.views.index', name="blog_index"),
	url(r'^about/$', 'blog.views.about', name="blog_about"),
	url(r'^reply/$', 'blog.views.reply',  name="blog_reply"),
	url(r'^category/(?P<slug>[\w]+)/$', 'blog.views.category', name="blog_category"),
	# url(r'^post/(?P<title>[\w]+)/$','blog.views.post'),
	url(r'^archives/$', 'blog.views.archives', name="blog_archives"),
	url(r'^article/(?P<slug>[-\w]+)/$', 'blog.views.article', name= "blog_article"),


)

urlpatterns += patterns('',
    url(r'^feeds/$', RSSFeed(), name='blog_feed'),
)

sitemaps = {  
    'post': BlogSitemap,       
}

urlpatterns += patterns('',
	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',{'sitemaps': sitemaps}),
)