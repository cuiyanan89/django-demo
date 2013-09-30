#_*_coding:utf-8_*_ 

from django.db import models

class UserModel(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

	def __unicode__(self):
		return self.username
