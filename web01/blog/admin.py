#_*_coding:utf-8_*_ 

from django.contrib import admin 
from blog.models import Nav, Shop

class ShopAdmin(admin.ModelAdmin):
	list_display =('shopname','address','phone1','phone2','status','last_ch_time')
	search_fields = ('shopname',)


admin.site.register(Nav)
admin.site.register(Shop,ShopAdmin)