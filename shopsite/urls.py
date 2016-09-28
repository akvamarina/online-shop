from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('shop.urls')),	#перенаправляет все запросы 'http://127.0.0.1:8000/' к shop.urls
]
