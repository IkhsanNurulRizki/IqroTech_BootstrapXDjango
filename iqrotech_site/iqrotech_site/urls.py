from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hero/', include('iqrotech_site.hero.urls')),
    path('langkah/', include('iqrotech_site.langkah.urls')),
    path('inti/', include('iqrotech_site.inti.urls')),
    path('tentang/', include('iqrotech_site.tentang.urls')),
]
