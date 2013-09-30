# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse

def login(request):
	username = request.GET['name']
	passwd = request.GET['passwd']

	return HttpResponse("welcome %s, sex %s" % (username,passwd))
