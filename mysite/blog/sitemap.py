#coding=utf8;

from django.contrib.sitemaps import Sitemap 
from blog.models import Post
from datetime import datetime

class BlogSitemap(Sitemap):

	changefreq = 'never'
	priority = 0.5

	def items(self):
		return Post.objects.all()

	def lastmod(self, item):
		return datetime.now()

