from django.conf.urls import include, url
from django.contrib import admin
import social.apps.django_app.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('shop.urls')),
    url('', include(social.apps.django_app.urls, namespace='social')),
]
