from django.db import models
from django.utils import timezone
import random
import string

class Product(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey('Category', to_field='name')
	description = models.TextField(default='')
	photo = models.URLField()
	price = models.PositiveIntegerField()
	quantity_on_stock = models.PositiveIntegerField()

	def __str__(self):
		return self.name
	

class Category(models.Model):
	COOKIES = 0
	CUPCAKES = 1
	CAKES = 2

	NAME_CHOICES = (
		(COOKIES, 'Печенье'),
		(CUPCAKES, 'Капкейк'),
		(CAKES, 'Торт'))

	name = models.IntegerField(choices=NAME_CHOICES, unique=True)

	def __str__(self):
		return self.NAME_CHOICES[self.name][1]


class Cart(models.Model):
	def generate_token():
		token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
			for x in range(40))
		return token

	user = models.ForeignKey('auth.User', null=True)
	token = models.CharField(max_length=40, default=generate_token)
	total_price = models.PositiveIntegerField(default=0)
	date_added = models.DateTimeField(default=timezone.now)
	archived = models.BooleanField(default=False)

	def add(self, product, quantity):
		product_cart, created = ProductCart.objects.get_or_create(cart=self, 
			product=product)
		product_cart.quantity += quantity
		product_cart.total_price += quantity * product.price
		product_cart.save()
		self.total_price += product_cart.total_price
		self.date_added = timezone.now()
		self.save()


class ProductCart(models.Model):
	cart = models.ForeignKey('Cart')	#по умолчанию привязывается по первичному ключу (id)
	product = models.ForeignKey('Product')
	quantity = models.PositiveIntegerField(default=0)
	total_price = models.PositiveIntegerField(default=0)
