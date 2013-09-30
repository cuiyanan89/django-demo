#_*_coding:utf-8_*_

from django.db import models

class News(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField(blank=True)
	img = models.FileField(upload_to='./imgs/')

	def __unicode__(self):
		return self.title


