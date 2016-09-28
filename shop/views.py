from django.shortcuts import render

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
	return render(request, 'shop/catalog/cookies.html', {})

def cupcakes(request):
	return render(request, 'shop/catalog/cupcakes.html', {})

def cakes(request):
	return render(request, 'shop/catalog/cakes.html', {})