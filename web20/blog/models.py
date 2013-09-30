#_*_coding:utf-8_*_ 

from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name 

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	create_time = models.DateTimeField(auto_now=True)

	category = models.ForeignKey(Category)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	content = models.TextField()
	create_time = models.DateTimeField(auto_now=True)

	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	class Meta:
		permissions = (
			("open_comment", "can create a comment"),
			("reply_comment", "can reply comment"),
			("close_comment", "can close commnet"),
		)
