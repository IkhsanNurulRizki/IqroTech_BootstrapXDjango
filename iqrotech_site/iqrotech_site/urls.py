from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hero/', include('hero.urls')),
    path('langkah/', include('langkah.urls')),
    path('inti/', include('inti.urls')),
    path('tentang/', include('tentang.urls')),
    path('testimoni/', include('testimoni.urls')),
    path('me/', include('me.urls')),

    url(r'^media/(?<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
