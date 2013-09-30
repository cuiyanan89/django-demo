#_*_coding:utf-8_*_ 

from django.contrib import admin
from blog.models import Post, Replay

admin.site.register(Post)
admin.site.register(Replay)