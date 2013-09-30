#_*_coding:utf-8_*_ 

from django.contrib import admin  
from blog.models import Category, Post, Reply

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)