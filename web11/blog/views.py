#_*_coding:utf-8_*_

from django.shortcuts import render, render_to_response
from blog.models import Nav, News

def index(request):
	nav_list = Nav.objects.all()
	nnav = []
	for nav in nav_list:
		k = nav.news_set.all()
		if 0<len(k):
			nnav.append(k[0])

	return render_to_response('index.html',{'nav_list': nav_list,'nnav':nnav})

def disp_nav(request, id=None):
	if id == None:
		nav_list = Nav.objects.all()
		return render_to_response('nav.html',{'nav_list':nav_list})
	nav_list = Nav.objects.all()
	nav = Nav.objects.get(id=id)
	return render_to_response('nav.html',{'nav':nav, 'nav_list':nav_list})

def post(request, id):

	news = News.objects.get(id=id)

	return render_to_response('post1.html',{'news':news})