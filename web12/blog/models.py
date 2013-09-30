#_*_coding:utf-8_*_ 

from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=30)
	img = models.FileField(upload_to='./img')

	def __unicode__(self):
		return self.name 

class Book(models.Model):
	name = models.CharField(max_length=30)
	publisher = models.CharField(max_length=30)
	auth_time = models.DateField()
	authors = models.ManyToManyField(Author)


	def __unicode__(self):
		return self.name