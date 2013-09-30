#_*_coding:utf-8_*_ 

from django import forms
from blog.models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','password')
		widgets = {
			'password': forms.PasswordInput(),
		}