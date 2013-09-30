
#_*_coding:utf-8_*_

from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=200)
	birthday = models.DateField(null=True)
	sex = models.CharField(max_length=1, choices=(('f','fmale'),('m','male')))
	regist_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.username
