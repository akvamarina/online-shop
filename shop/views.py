from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Category


def main_page(request):
	return render(request, 'shop/main_page.html', {})

def sales(request):
	return render(request, 'shop/sales.html', {})

def delivery(request):
	return render(request, 'shop/delivery.html', {})

def contacts(request):
	return render(request, 'shop/contacts.html', {})

def cart(request):
	return render(request, 'shop/cart.html', {})

def cookies(request):
	cookies_list = Product.objects.filter(category=Category.COOKIES)
	return render(request, 'shop/catalog/cookies.html', {'cookies_list': cookies_list})

def cupcakes(request):
	cupcakes_list = Product.objects.filter(category=Category.CUPCAKES)
	return render(request, 'shop/catalog/cupcakes.html', {'cupcakes_list': cupcakes_list})

def cakes(request):
	cakes_list = Product.objects.filter(category=Category.CAKES)
	return render(request, 'shop/catalog/cakes.html', {'cakes_list': cakes_list})

@login_required
def account_profile(request):
    return HttpResponse("Hello, {0}! Nice to meet you.".format(request.user.first_name))

def account_logout(request):
    logout(request)
    return redirect('/') 
