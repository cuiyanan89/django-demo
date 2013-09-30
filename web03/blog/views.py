# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Picture
import os

def index(request):
	pic_list = Picture.objects.all()
	# path = os.path.dirname(os.path.dirname(__file__))
	# path = os.path.join(path,'upload')
	# imgs = os.listdir(path)
	# for i in range(len(imgs)):
	# 	imgs[i] = os.path.join(path,imgs[i])


	return render_to_response('index.html',{'pic_list': pic_list})