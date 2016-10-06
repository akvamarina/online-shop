from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
import time
import datetime
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm


def main_page(request):
    return render(request, 'shop/main_page.html', {})

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

@csrf_protect
def account_login(request):
    if request.user.is_authenticated():
        return redirect('/accounts/profile/')
    if request.method == "POST":
        auth_user_form = AuthUserForm(request.POST)
        for key in request.POST:
            print(key, request.POST[key])
        if not auth_user_form.is_valid():
            return render(request, 'shop/accounts/login.html', 
                {"auth_user_form": auth_user_form})
        user_model = auth_user_form.save(commit=False)
        #аккаунт привязан к email (без имени пользователя)
        user = authenticate(username=user_model.email,
            password=user_model.password)
        if user is not None:
            login_user(request, user)
            return redirect('/accounts/profile/')
    auth_user_form = AuthUserForm()
    return render(request, 'shop/accounts/login.html', {"auth_user_form": auth_user_form})

@csrf_protect
def account_signup(request):
    if request.user.is_authenticated():
        return redirect('/accounts/profile/')
    if request.method == "POST":
        create_user_form = CreateUserForm(request.POST)
        for key in request.POST:
            print(key, request.POST[key])
        if not create_user_form.is_valid():
            return render(request, 'shop/accounts/signup.html', 
                {"create_user_form": create_user_form})
        user = create_user_form.save()
        # login_user(request, user)
        return redirect('/accounts/login/')
    create_user_form = CreateUserForm()
    return render(request, 'shop/accounts/signup.html', {"create_user_form": create_user_form})

def login_user(request, user):
    before_login_cart = get_cart(request)
    login(request, user)
    if before_login_cart.total_price > 0:
        before_login_cart.user = user
        before_login_cart.save()

@login_required
def account_profile(request):
    return render(request, 'shop/accounts/profile.html', {})

@login_required
def account_logout(request):
    #если пользователь вышел, не завершив заказ, корзина не сохраняется
    if Cart.objects.filter(user=request.user, archived=False).exists():
        Cart.objects.filter(user=request.user, archived=False).delete()
    logout(request)
    return redirect('/') 

def cart(request):
    cart = get_cart(request)
    product_cart_list = ProductCart.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'cart': cart, 'product_cart_list': product_cart_list})

def get_cart(request):
    if request.user.is_authenticated():
        if Cart.objects.filter(user=request.user, archived=False).exists():
            return Cart.objects.filter(user=request.user, archived=False).latest('date_added')
        return Cart.objects.create(user=request.user)
    if 'token' in request.session:
        return Cart.objects.filter(token=request.session['token']).latest('date_added')
    cart = Cart.objects.create(user=None)
    request.session['token'] = cart.token
    return cart

def del_product(request, product_cart_id):
    cart = get_cart(request)
    cart.delete(product_cart_id)
    product_cart_list = ProductCart.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'cart': cart, 'product_cart_list': product_cart_list})

@login_required
def payment_pay(request):
    cart = get_cart(request)
    product_cart_list = []
    for product_cart in ProductCart.objects.filter(cart=cart):
        product_cart_list.append(product_cart.product.name)
    paypal_dict = {
        "business": "bird-cherry-bakery@bk.ru",
        "amount": cart.total_price,
        "currency_code": "RUB",
        "item_name": product_cart_list,
        "invoice": "INV-" + str(int(time.time())),
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://127.0.0.1:8000/payment/success/",
        "cancel_return": "http://127.0.0.1:8000/payment/cart/",
        "custom": str(request.user.username)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'shop/payment/pay.html', 
        {'form': form, 'paypal_dict': paypal_dict})

@csrf_exempt
def payment_success(request):
    cart = get_cart(request)
    cart.archived = True;
    cart.save()
    return render(request, 'shop/payment/success.html', {})