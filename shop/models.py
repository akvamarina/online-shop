from django.db import models

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




# class Customer(models.Model):
# 	email = models.TextField(max_length=100)
# 	password = models.TextField(max_length=20)
# 	cart = models.		