from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hero/', include('hero.urls')),
    path('langkah/', include('langkah.urls')),
    path('inti/', include('inti.urls')),
    path('tentang/', include('tentang.urls')),
    # path('testimoni/', include('testimoni.urls')),
    # path('me/', include('me.urls')),
]
