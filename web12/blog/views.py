#_*_coding:utf-8_*_ 

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from blog.models import Author, Book 

def authors(request):
	authors = Author.objects.all()

	return render_to_response('AuthorAndBook.html',{'authors':authors,'flag':'Author'}) 

def books(request):
	books = Book.objects.all()
	return render_to_response('AuthorAndBook.html',{'books':books,'flag':'Book'})

def author(request,name):
	author = Author.objects.get(name=name) 
	books = author.book_set.all()
	return render_to_response('author.html',{'books':books,'author':author})

def book(request, name):
	book = Book.objects.get(name=name)
	authors = book.authors.all()
	return render_to_response('book.html',{'authors':authors,'book':book})
