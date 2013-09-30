#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html',{'posts':posts})

def post(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		if title == '':
			return render(request,'post.html',{})
		Post.objects.create(title=title,content=content)
		return HttpResponseRedirect('/index/')
	else:
		return render(request,'post.html',{})

def post_cont(request,id=id):

	post = Post.objects.get(id=id)
	return render(request,'post_cont.html',{'post':post})

def post_change(request,id=id):

	post = Post.objects.get(id=id)

	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		post.title = title
		post.content = content
		post.save()
		return HttpResponseRedirect('/index/')
	else:
		return render(request,"post.html",{'post':post})

def post_del(request,id=id):

	post = Post.objects.get(id=id)
	post.delete()
	return HttpResponseRedirect('/index/')