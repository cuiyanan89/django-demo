#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login 
from blog.forms import UserForm, LoginForm

def index(request):
	if request.user.is_authenticated():
		return render_to_response('index.html',{'user':request.user})
def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			uf.instance.set_password(uf.instance.password)
			uf.instance.is_staff = True
			uf.save()
			return HttpResponse('ok')
	else:
		uf = UserForm()
	return render(request,'register.html',{'uf':uf})

def login_u(request):

	if request.method == 'POST':
		uf = LoginForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user:
				# request.session['user'] = user
				login(request, user)
				return HttpResponseRedirect('/index/')
			return HttpResponse('no')
	else:
		uf = LoginForm()
	return render(request,'register.html',{'uf':uf})