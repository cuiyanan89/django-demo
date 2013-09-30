#_*_coding:utf-8_*_ 

from django.db import models
from django.contrib.auth.models import User



class Nav(models.Model):
	title = models.CharField(max_length=10,verbose_name=u"分类")

	def __unicode__(self):
		return self.title

class Shop(models.Model):
	shopname = models.CharField(max_length=30,verbose_name=u"店名")
	descript = models.CharField(max_length=200,verbose_name=u"描述")
	address = models.CharField(max_length=100,verbose_name=u"地址")
	phone1	= models.CharField(max_length=11,verbose_name=u"电话1")
	phone2	= models.CharField(max_length=11,verbose_name=u"电话2")
	attrs = models.CharField(default=111,max_length=3,verbose_name=u"属性")
	count = models.IntegerField(default=0,max_length=6,verbose_name=u"人气")
	status = models.BooleanField(default=True,verbose_name=u"状态")
	regist_time = models.DateTimeField(auto_now=True,verbose_name=u"注册时间")
	last_ch_time = models.DateTimeField(verbose_name=u"最后修改时间")
	change_user = models.OneToOneField(User,verbose_name=u"最后修改用户")

	nav = models.ForeignKey(Nav,verbose_name=u"分类")

	def __unicode__(self):
		return self.shopname
