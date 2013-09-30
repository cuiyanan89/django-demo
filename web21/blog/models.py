#_*_coding:utf-8_*_ 

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name 

class Post(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()

	auth = models.ForeignKey(User)
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return self.title 

class Reply(models.Model):

	content = models.TextField()

	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)


