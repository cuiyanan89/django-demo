#_*_coding:utf-8_*_ 

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=20)

	def __unicode__(self):
		return self.title

class Replay(models.Model):
	title = models.CharField(max_length=20)

	def __unicode__(self):
		return self.title

