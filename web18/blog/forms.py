#_*_coding:utf-8_*_ 

from django import forms
from django.contrib.auth.models import User 
from blog.models import Employee

class UserForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=200,widget=forms.PasswordInput)
	tel = forms.CharField(max_length=11	)
	address = forms.CharField(max_length=100,required=False)
	headImg = forms.FileField()



class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=200,widget=forms.PasswordInput)