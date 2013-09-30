#_*_coding:utf-8_*_ 

from django import forms
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from blog.models import Product
from blog.forms import ProductForm    

def index(reqeust):
    return HttpResponse("hello python")

def create_product(request):
   #创建产品de 视图函数 
    pro_form = ProductForm(reqeust.POST or None)
    if pro_form.is_valid():
        pro_form.save()
    t = get_template('blog/create_product.html')  
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def list_product(request):
   #商品的显示与分页 
    list_items = Product.objects.all()
    paginator = Paginator(list_items, 10)

    try:
        page = int(reqeust.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except:
        list_items = paginator.page(paginator.num_pages)

    t = get_template('blog/list_product.html')
    c = RequestContext(request, local())
    return HttpResponse(t.render(c))

def view_product(request, id):
    
    product_instance = Product.objects.get(id = id)
    t = get_template('blog/views.product.html')
    c = ReqeustContext(request, local())
    return HttpResponse(t.render(c))

def edit_product(request, id):
    
    product_instance = Product.objects.get(id = id)
    pro_form = ProductForm(request.POST or None, instance = product_instance)
    if pro_form.is_valid():
        pro_form.save()
        
    t = get_template('blog/edit_product')
    c = RequestContext(request, local())
    return HttpResponse(t.render(c))
