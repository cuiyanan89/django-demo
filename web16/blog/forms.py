#_*_coding:utf-8_*_ 

from django import forms
from blog.models import UserModel

class UserForm(forms.ModelForm):
	# username = forms.CharField(max_length=20,label="用户名",validators=[valid])
	# password = forms.CharField(min_length=6,widget=forms.PasswordInput,label="密码")
	
	class Meta:
		model = UserModel
		fields = ("username","password",)
		widgets ={
			'password': forms.PasswordInput(),
		}