from django.conf.urls import include, url
from . import views		#импорт всех представлений из приложения shop
import paypal.standard.ipn.urls
import django.contrib.auth.views as auth_views


urlpatterns = [
	url(r'^$', views.main_page, name='main_page'),
	url(r'^delivery/$', views.delivery, name='delivery'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^cart/delete(?P<product_cart_id>[0-9]+)/$', views.del_product, name='del_product'),
	url(r'^catalog/cookies/$', views.cookies, name='cookies'),
	url(r'^catalog/cupcakes/$', views.cupcakes, name='cupcakes'),
	url(r'^catalog/cakes/$', views.cakes, name='cakes'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
	# auth
	url(r'^accounts/login/$', views.account_login, name='login'),
	url(r'^accounts/signup/$', views.account_signup, name='signup'),
	url(r'^accounts/logout/$', views.account_logout, name='logout'),
 	url(r'^accounts/profile/$', views.account_profile, name='profile'),
    # pay
    url(r'^payment/pay/$', views.payment_pay, name='pay'),
    url(r'^payment/success/$', views.payment_success, name='success'),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
]
