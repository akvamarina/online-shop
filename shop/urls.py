from django.conf.urls import url	#импорт всех методов django
from . import views		#импорт всех представлений из приложения shop

urlpatterns = [
	url(r'^$', views.main_page, name='main_page'),
	url(r'^sales/$', views.sales, name='sales'),
	url(r'^delivery/$', views.delivery, name='delivery'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^catalog/cookies/$', views.cookies, name='cookies'),
	url(r'^catalog/cupcakes/$', views.cupcakes, name='cupcakes'),
	url(r'^catalog/cakes/$', views.cakes, name='cakes'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
	url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),
]