#_*_coding:utf-8_*_ 

from django.db import models
from django.db.models import permalink
from django.utils import timezone
from markdown import markdown

class Category(models.Model):
	#  分类表
	name = models.CharField(max_length=10,verbose_name=u"名称") #分类名称
	slug = models.CharField(max_length=50, unique=True, verbose_name=u'Slug') #路由字段

	def __unicode__(self):
		return self.name

	@permalink                                           #绝对路径，通过 objects.get_absolute_url直接访问视图
	def get_absolute_url(self):
		return ('blog_category',None, {'slug':self.slug}) #第一个为路由名称，第三个参数为设置路由

	class Meta:
		ordering = ['id']  #排序按升序 将序为['-id']
		verbose_name_plural = verbose_name = u'分类' #在后台添加有好的表明

class Article(models.Model):
	#  文章
	title = models.CharField(max_length=100,verbose_name=u'标题')
	slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Slug') #unique 表示字段唯一
	contents = models.TextField(verbose_name=u'内容')
	contents_html = models.TextField(blank=True, null=True,verbose_name=u'渲染内容') #blank & null = True 表示如果不写入数据库中表示为kong
	create_time = models.DateTimeField(auto_now=True,verbose_name=u"发表日期")
	modify_time = models.DateTimeField(default=timezone.now, verbose_name=u"修改日期")
	allow_comment = models.BooleanField(default=False, verbose_name=u"允许评论")
	counts = models.IntegerField(default=0,verbose_name=u'点击数')

	category = models.ForeignKey(Category, verbose_name=u'分类')

	def __unicode__(self):
		return self.title
	def click_once(self):
		self.counts += 1
		super(Article, self).save(update_fields=['counts',])

	@permalink
	def get_absolute_url(self):
		return ('blog_article',None,{'slug':self.slug})

	def save(self):
		self.contents_html = markdown(self.contents, ['codehilite'])  #利用markdown渲染出contents内容，contents_html为渲染内容
		super(Article,self).save()  #调用父类保存

	class Meta:
		get_latest_by = 'create_time'   
		ordering = ['-id']
		verbose_name_plural = verbose_name = u'文章'

class Link(models.Model):
	# friends Link 
	name = models.CharField(max_length=30, verbose_name=u"名称")
	link = models.URLField(max_length=100, verbose_name=u"链接")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = verbose_name = u'链接'
