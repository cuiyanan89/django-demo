#_*_coding:utf-8_*_ 

from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import User
import hashlib


def login(request):
	
	if request.method == 'POST':
		email = request.POST.get('email','')
		try:
			user = User.objects.get(email=email)
			
			passwd = request.POST.get('passwd','')
			passwd = hashlib.sha1(user.username+passwd).hexdigest()
			if passwd == user.passwd:
				return HttpResponseRedirect('/success/')
		except:
			if email == '':
				return render(request,'login.html',{})
			return HttpResponse("invalid email or password")

	return render(request,'login.html',{})

def regist(request):

	if request.method == "POST":
		email = request.POST.get('email','')
		try:
			User.objects.get(email=email)
		except:
			passwd = request.POST.get('passwd','')
			print passwd
			username = request.POST.get('username','')
			passwd = hashlib.sha1(username+passwd).hexdigest()
			User.objects.create(username=username,email=email,passwd=passwd)
			return HttpResponseRedirect('/login/')
		return HttpResponse("invalid email")
	else:
		return render(request,'regist.html',{})

def success(request):

	return HttpResponse("ok")
