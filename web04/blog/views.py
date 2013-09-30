#_*_coding:utf-8_*_ 

from django.shortcuts import render_to_response
from blog.models import Picture

def index(request):
	picture = Picture.objects.all()
	return render_to_response('index.html',{'picture': picture})

def display_pic(request, id, name):
	print id , name
	pic = Picture.objects.get(id=id)
	# pic = Picture.objects.filter(id=req)

	return render_to_response('display_pic.html',{'pic':pic})

def show(request, template_name):

	return render_to_response(template_name,{'content':"aaaaaaa"})