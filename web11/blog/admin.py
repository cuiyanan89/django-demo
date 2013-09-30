#_*_coding: utf-8_*_ 

from django.contrib import admin
from blog.models import Nav, News

admin.site.register(Nav)
admin.site.register(News)