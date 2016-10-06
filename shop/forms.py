# from django.db import models
from django import forms
from .models import ProductCart
from django.contrib.auth.models import User

class ProductCartForm(forms.ModelForm):


	class Meta:
		model = ProductCart
		fields = ('quantity',)
		labels = {
            'quantity': 'Количество',
        }



class AuthUserForm(forms.ModelForm):


	class Meta:
		model = User
		fields = ('email', 'password',)
		widgets = {
			'password': forms.PasswordInput,
		}



# class CreateUserForm(forms.ModelForm):


# 	class Meta:
# 		model = User
# 		fields = ('')


