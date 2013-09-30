#_*_coding:utf-8_*_

from django.http import HttpResponse

def show(request):
    
    return HttpResponse(request.path)