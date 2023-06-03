from django.urls import path
from django.contrib import admin
from django.urls.conf import include  
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('', views.home, name = 'home'),
    path('notification', views.notify, name = 'notify'),
    path('guide', views.guide, name = 'guide')
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)