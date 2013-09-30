#_*_coding:utf-8_*_ 

from django.shortcuts import render_to_response, render 
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import UserForm
from blog.models import UserModel
import hashlib



def register(request):
	if request.method == 'POST':

		uf = UserForm(request.POST, request.FILES)
		if uf.is_valid():
			um = UserModel()
			um.username = uf.cleaned_data['username']
			um.password = hashlib.sha1(uf.cleaned_data['username']+uf.cleaned_data['password']).hexdigest()
			um.email	= uf.cleaned_data['email']
			um.birthday = uf.cleaned_data['birthday']
			um.headimg	= uf.cleaned_data['headimg']
			um.descript = uf.cleaned_data['descript']
			um.save()
			return HttpResponse('ok')
	else:
		uf = UserForm()
	return render(request,'register.html',{'uf':uf})


