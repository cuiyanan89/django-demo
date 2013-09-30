#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Post, Reply
from blog.forms import UserForm


def index(request):
	limit = 2
	post = Post.objects.all()
	p = Paginator(post, limit)
	page = request.GET.get('page')

	try:
		contacts = p.page(page)
	except PageNotAnInteger:
		contacts = p.page(1)
	except EmptyPage:
		contacts = p.page(p.num_pages)
	
	return render(request, 'index.html', {'contacts': contacts, 'user': request.user})

def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.create_user(username = username)
			user.set_password(password)
			user.save()
			return HttpResponseRedirect('/index/')
	else:
		uf = UserForm()
	return render(request, 'register.html', {'uf': uf})

def post(request, id):
	post = Post.objects.get(id = id)

	if request.method == 'POST':
		reply = request.POST.get('reply')
		post.reply_set.create(content = reply,user=request.user)
	return render(request, 'index.html', {'post': post, 'user':request.user})

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		print username
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse(username)
		else:
			return HttpResponse('')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/index/')