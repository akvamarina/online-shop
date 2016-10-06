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



class CreateUserForm(forms.ModelForm):
	confirm_password = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ('email', 'password',)
		widgets = {
			'password': forms.PasswordInput,
		}

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(username=email).exists():
			raise forms.ValidationError("E-mail уже зарегистрирован")
		return email

	#проверка корректности поля confirm_password (выполняется при вызове is_valid())
	def clean_confirm_password(self):
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("confirm_password")
		if password and confirm_password and password != confirm_password:
			raise forms.ValidationError("Пароли не совпадают")
		return confirm_password

	def save(self, commit=True):
		#вызов "основного" (не переопределенного) метода save
		user = super(CreateUserForm, self).save(commit=False)
		user.username = user.email
		user.set_password(self.cleaned_data.get("password"))
		if commit:
			user.save()
		return user;