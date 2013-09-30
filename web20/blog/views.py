#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post,Comment
from blog.forms import UserForm

def index(request):
	limit = 1    # zuida duixiang shu
	post = Post.objects.all()
	p = Paginator(post,limit)
	page = request.GET.get('page')
	try:
		contacts = p.page(page)
	except PageNotAnInteger:
		contacts = p.page(1)
	except EmptyPage:
		contacts = p.page(p.num_pages)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)	
			return HttpResponse(username)
		else:
			return HttpResponse('')
	return render(request,'index.html',{'contacts':contacts,'user':request.user})

def login_user(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/index/')
	else:
		uf = UserForm()
	return render(request,'login.html',{'uf':uf})

def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.create_user(username=username)
			user.set_password(password)
			user.user_permissions.add('open_comment','reply_comment','close_comment')
			user.save()
			return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render(request,'login.html',{'uf':uf})

def post(request,id):
	content = Post.objects.get(id=id)
	
	if request.user.is_authenticated() and request.user.has_perm('blog.open_comment'):
		if request.method == "POST":
			comment = request.POST.get('comment',None)
			if comment is not None:
				content.comment_set.create(content=comment)
		comment_list = content.comment_set.all()
		return render(request,'index.html',{'content':content,'comment_list':comment_list})
	comment_list = content.comment_set.all()
	return render(request,'index.html',{'content':content,'comment_list':comment_list})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/index/')

