#_*_coding:utf-8_*_ 

from django.contrib import admin
from blog.models import Category, Article, Link

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']  #在admin中只显示 name 字段
	prepopulated_fields = {'slug': ('name',)}  #slug 自动填充name字段

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title','slug','counts','category','create_time']
	list_filter = ['title']   #通过title 过滤
	prepopulated_fields = {'slug':('title',)}
	# yu tianchong

class LinkAdmin(admin.ModelAdmin):
	list_display = ['name','link']

admin.site.register(Category,CategoryAdmin)  #设置modelsAdmin来注册模型
admin.site.register(Article,ArticleAdmin)
admin.site.register(Link,LinkAdmin)

