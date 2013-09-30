#_*_coding:utf-8_*_ 

from django.contrib import admin 
from blog.models import User, Menu, Food

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Food)