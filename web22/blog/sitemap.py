#coding=utf8;

from django.contrib.sitemaps import Sitemap
from blog.models import Article

class BlogSitemap(Sitemap):  
    #此处都为比选项
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.modify_time