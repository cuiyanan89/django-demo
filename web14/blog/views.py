#_*_coding:utf-8_*_ 

from django.shortcuts import render_to_response, render 
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import UserForm
from blog.models import UserModel
from django.core.exceptions import ObjectDoesNotExist
import hashlib

def index(request):
	return HttpResponse('welcome %s' % request.COOKIES['username'])


def register(request):
	if request.method == 'POST':

		uf = UserForm(request.POST)
		if uf.is_valid():
		    uf.instance.password = hashlib.sha1(uf.instance.password+uf.instance.username).hexdigest()
		    uf.save()
		    return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render(request,'register.html',{'uf':uf})


def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = hashlib.sha1(uf.cleaned_data['password']+username).hexdigest()
			try:
				UserModel.objects.get(username=username,password=password)
				response = HttpResponseRedirect('/index/')
				response.set_cookie(key='username',value=username)
				return response
			except ObjectDoesNotExist:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render(request,'login.html',{'uf':uf})