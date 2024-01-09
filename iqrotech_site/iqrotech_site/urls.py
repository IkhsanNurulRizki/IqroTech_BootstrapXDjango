from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('iqrotech_site/hero/', include('iqrotech_site.hero.urls')),
    path('iqrotech_site/langkah/', include('iqrotech_site.langkah.urls')),
    path('iqrotech_site/inti/', include('iqrotech_site.inti.urls')),
    path('iqrotech_site/tentang/', include('iqrotech_site.tentang.urls'))
]
