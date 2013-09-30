#_*_coding:utf-8_*_ 

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import User
import hashlib
import time


def register(request):
	
	if request.method == 'POST':		
		username = request.POST.get('username','')
		try:
			User.objects.get(username=username)
		except:
			passwd = request.POST.get('password','')
			birthday = request.POST.get('birthday','')
			sex = request.POST.get('sex','')
			regist_time = time.ctime()
			passwd = hashlib.sha1(username+passwd).hexdigest()
			User.objects.create(username=username,password=passwd,sex=sex,birthday=birthday,
				regist_time=regist_time)
		return HttpResponseRedirect("/login/")

	else:
		return render(request,'register.html',{})


def login(request):

	if request.method == "GET":
		return render(request,'login.html',None)
	else:
		username = request.POST.get('username','')
		try:
			user = User.objects.get(username=username)
			passwd = request.POST.get('password', '')
			passwd = hashlib.sha1(username+passwd).hexdigest()
			if passwd == user.password:
				return HttpResponse('ok')
		except:
			return HttpResponse("username is not found")

		


	