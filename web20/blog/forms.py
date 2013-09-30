#_*_coding:utf-8_*_ 

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=200,widget=forms.PasswordInput)

class CommentForm(forms.Form):
	comment =  forms.CharField(widget=forms.Textarea)
	
