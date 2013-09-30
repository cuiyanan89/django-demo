#_*_coding:utf-8_*_ 

from django.db import models

class UserModel(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	birthday = models.DateField(blank=True)
	headimg = models.FileField(upload_to='./imgs')
	descript = models.TextField()

	def __unicode__(self):
		return self.username
