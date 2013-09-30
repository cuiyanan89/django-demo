#_*_coding:utf-8_*_
import json 
#from django.http import HttpResponse
#from django.template import loader, Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Diary
import os

COUNT = 1

""" 导入两种模块, loader 和 Context 用来渲染模板 """

#def index(request):
#    t = loader.get_template('index.html')                 #获取模板对象
#    c = Context({'name':'kmean','title':'index'})         #生成context对象
#    r = t.render(c)                                       #渲染模板文件
#    return HttpResponse(r)

def index(request):
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path,'static/imgs/')
    imgs = os.listdir(path)
    for i in range(len(imgs)):
        imgs[i] = os.path.join('/static/imgs',imgs[i])
        
    # text = json.dumps({'diary':{'title':diary.title,'content':diary.content}})
    return render_to_response('index.html',{'imgs':imgs})

def tjson(request):
    global COUNT 
    if COUNT< Diary.objects.count():

        COUNT += 1
    else:
        COUNT = 1
    diary = Diary.objects.all()[COUNT-1]
    text = json.dumps({'title':diary.title,'content':diary.content})
    return HttpResponse(text)
    
def ajax(request):

	return render_to_response("tjson.html",{})