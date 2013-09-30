#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from blog.models import Employee
from blog.forms import UserForm, LoginForm

def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST,request.FILES)
		if uf.is_valid():
			user = User.objects.create_user(username=uf.cleaned_data['username'],email="123@123.com")
			user.set_password(uf.cleaned_data['password'])
			user.save()
			Employee.objects.create(user=user,tel=uf.cleaned_data['tel'],address=uf.cleaned_data['address'],headImg=uf.cleaned_data['headImg'])
			return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render(request,'register.html',{'uf':uf})

def login_u(request):
	if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			print username
			print password

			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/index/')
			return HttpResponse('no')
	else:
		return render(request,'login.html',{})

def index(request):
	if request.user.is_authenticated():
		return render(request,'login.html',{'user':request.user})
	return HttpResponse('not session ')

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login/')