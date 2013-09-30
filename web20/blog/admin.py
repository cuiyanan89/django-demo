#_*_coding:utf-8_*_ 

from django.contrib import admin 
from blog.models import Post, Category, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)