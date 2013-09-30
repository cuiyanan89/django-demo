#_*_coding:utf-8_*_ 

from django import forms 

class UserForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=100,widget=forms.PasswordInput)