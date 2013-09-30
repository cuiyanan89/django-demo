
from django.db import models
from django.contrib import admin

class Diary(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	def __unicode__(self):
		return self.title

admin.site.register(Diary)