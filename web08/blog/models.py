#_*_coding:utf-8_*_ 

from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	passwd = models.CharField(max_length=100)
	regist_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.username