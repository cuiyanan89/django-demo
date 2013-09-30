#_*_coding:utf-8_*_  

from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def index(request,name):

	return render_to_response('%s.html' % name	,{})