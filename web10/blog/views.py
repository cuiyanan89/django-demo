#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Replay

def index(request):
	posts = Post.objects.all()

	return render(request,'index.html',{'posts':posts})

def post(request):
	
	if request.method == 'POST' :
		title = request.POST['title'] 
		content = request.POST['content']
		if title == '':
			return render(request,'post.html',{})
		Post.objects.create(title=title, content=content)
		return HttpResponseRedirect('/index/')
	else:
		return render(request,'post.html',{})

def post_cont(request,id=id):
	
	post = Post.objects.get(id=id)

	if request.method == 'POST':
		content = request.POST.get('content','')
		if content == '':
			return render(request,'post_cont.html',{'post':post})
		post.replay_set.create(content=content)
		
	replay = post.replay_set.all()
	return render(request,'post_cont.html',{'post':post,'replay':replay})
	