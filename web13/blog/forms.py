#_*_coding:utf-8_*_ 

from django import forms
from django.core.exceptions import ValidationError
import re

def valid(value):
	if re.search(r'\d',value):
		raise ValidationError(u'用户名不得包含数字')

class UserForm(forms.Form):
	username = forms.CharField(max_length=20,label="用户名",validators=[valid])
	password = forms.CharField(min_length=6,widget=forms.PasswordInput,label="密码")
	email = forms.EmailField(required=False,label="邮箱")
	birthday = forms.DateField(required=False,label="出生日期")
	headimg = forms.FileField(label="头像")
	descript = forms.CharField(max_length=200,widget=forms.Textarea,label="自我描述")

