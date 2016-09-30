from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Category
from .models import Cart
from .models import ProductCart
from .forms import ProductCartForm
# from cart.cart import Cart


def main_page(request):
	return render(request, 'shop/main_page.html', {})

def sales(request):
	return render(request, 'shop/sales.html', {})

def delivery(request):
	return render(request, 'shop/delivery.html', {})

def contacts(request):
	return render(request, 'shop/contacts.html', {})

def cookies(request):
	cookies_list = Product.objects.filter(category=Category.COOKIES)
	return render(request, 'shop/catalog/cookies.html', {'cookies_list': cookies_list})

def cupcakes(request):
	cupcakes_list = Product.objects.filter(category=Category.CUPCAKES)
	return render(request, 'shop/catalog/cupcakes.html', {'cupcakes_list': cupcakes_list})

def cakes(request):
	cakes_list = Product.objects.filter(category=Category.CAKES)
	return render(request, 'shop/catalog/cakes.html', {'cakes_list': cakes_list})

def product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	if request.method == "POST":
		form = ProductCartForm(request.POST)
		if form.is_valid():
			product_cart = form.save(commit=False)
			cart = get_cart(request)
			cart.add(product, product_cart.quantity)
	form = ProductCartForm(initial={'quantity': 1})
	return render(request, 'shop/catalog/product.html', {'product': product, 'form': form})

@login_required
def account_profile(request):
    return HttpResponse("Hello, {0}! Nice to meet you.".format(request.user.first_name))

def account_logout(request):
    logout(request)
    return redirect('/') 

def cart(request):
	cart = get_cart(request)
	product_cart_list = ProductCart.objects.filter(cart=cart)
	return render(request, 'shop/cart.html', {'cart': cart, 'product_cart_list': product_cart_list})

def get_cart(request):
	if request.user.is_authenticated():
		if Cart.objects.filter(user=request.user).exists():
			return Cart.objects.filter(user=request.user).latest('date_added')
		return Cart.objects.create(user=request.user)
	if 'token' in request.session:
		return Cart.objects.filter(token=request.session['token']).latest('date_added')
	cart = Cart.objects.create(user=None)
	request.session['token'] = cart.token
	return cart