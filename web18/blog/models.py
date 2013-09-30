#_*_coding:utf-8_*_ 
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
	user = models.OneToOneField(User)
	tel = models.CharField(max_length=11,verbose_name=u'tel')
	address = models.CharField(max_length=100,verbose_name=u'address')
	headImg = models.FileField(upload_to='./imgs/')
