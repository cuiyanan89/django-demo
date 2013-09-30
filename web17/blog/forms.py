#_*_coding:utf-8_*_ 

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

	username = forms.CharField(max_length=20)
	class Meta:
		model = User
		fields = ('username','email','password')
		widgets = {
			'password':forms.PasswordInput()
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=100,widget=forms.PasswordInput)