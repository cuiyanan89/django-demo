#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import UserForm
from django.core.exceptions import ObjectDoesNotExist
from blog.models import User, Menu, Food
import hashlib

def index(request):

	menus = Menu.objects.all()

	return render(request,'index.html',{'menus':menus,'username':request.COOKIES['username']})

def login(request):

	if request.method == 'POST':
		# username = request.POST['username']
		# password = request.POST['password']
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.instance.username
			password = uf.instance.password
			password = hashlib.sha1(username+password).hexdigest()
			try:
				User.objects.get(username=username,password=password)
				response = HttpResponseRedirect('/index/')
				response.set_cookie(key='username',value=username)
				return response
			except ObjectDoesNotExist:
				print "not found"

	return render(request,'login.html',{})

def register(request):

	if request.method == "POST":
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.instance.username
			password= uf.instance.password
			uf.instance.password = hashlib.sha1(username+password).hexdigest()
			uf.save()

			response = HttpResponseRedirect('/login/')
			# response.set_cookie(key='username',value=username)
			return response
	else:
		uf = UserForm()
	return render(request,'register.html',{'uf':uf})

def menu(request,id):

	menus = Menu.objects.all()
	menulist = Menu.objects.get(id=id)

	return render(request,'menu.html',{'menulist':menulist,'menus':menus,'username':request.COOKIES['username']})

