#coding:utf8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Article

class RSSFeed(Feed):
	title = "danpy5 news"
	link = "/"
	description = "Update on changes"

    #三个函数为比选项
	def items(self):
		return Article.objects.order_by('-create_time').all()[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.contents_html




