#_*_coding:utf-8_*_ 

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import ArticleForm
from blog.models import Article, Category, Link




def common_response(reqeust):

	common = {
		'category_list' : Category.objects.all(),
		'link_list'		: Link.objects.all(),

	}
	return common

def index(request):
	article_list = Article.objects.all()

	paginator = Paginator(article_list,5)  #分页器，每页有5个内容
	page = request.GET.get('page')         #获取当前页数

	try:
		contacts = paginator.page(page) #尝试获取页数中的article内容
	except PageNotAnInteger:
		contacts = paginator.page(1) # 页数不存在则跳到第一页
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages) #空的页数则跳到最后一页

	data = {'contacts': contacts}
	data.update(common_response(request))

	return render(request,'index.html',data)

def category(request,slug):

	cur_category = get_object_or_404(Category,slug=slug) #获取分页对象或抛出异常
	contacts = cur_category.article_set.all()
	data = {'contacts':contacts, 'category': cur_category}
	data.update(common_response(request))
	return render(request,'index.html',data)

def about(request):
	data = {'comments':True}
	data.update(common_response(request))
	return render_to_response('about.html', data)

def reply(request):
	data = {'comments':True}
	data.update(common_response(request))

	return render_to_response('reply.html', data)

def archives(request):
	article_list = Article.objects.order_by('-id').all() #根据id的将序排出来
	data = {'article_list':article_list}
	data.update(common_response(request))

	return render_to_response('archives.html', data)

def article(request,slug):

	article = Article.objects.get(slug=slug)
	data = {'article':article, 'comments':True}
	data.update(common_response(request))
	article.click_once()

	return render_to_response('article.html', data)

