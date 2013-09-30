from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name 

class Book(models.Model):
	title = models.CharField(max_length=30)
	author = models.ManyToManyField(Author, through='BookAuthor')

	def __unicode__(self):
		return self.title

class BookAuthor(models.Model):
	book = models.ForeignKey(Book)
	author = models.ForeignKey(Author)
	create_at = models.DateTimeField(auto_now=True)
	