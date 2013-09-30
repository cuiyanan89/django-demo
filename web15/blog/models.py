#_*_coding:utf-8_*_ 

from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20,verbose_name="name")
	password = models.CharField(max_length=100,verbose_name="mima")

	def __unicode__(self):
		return self.username

class Menu(models.Model):
	title = models.CharField(max_length=10)

	def __unicode__(self):
		return self.title

class Food(models.Model):
	title = models.CharField(max_length=30,verbose_name="caiming")
	img = models.FileField(upload_to="./imgs/")
	price = models.CharField(max_length=3, verbose_name="jiage")
	menu = models.ForeignKey(Menu)

	def __unicode__(self):
		return self.title
