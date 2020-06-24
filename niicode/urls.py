from django.contrib import admin
from django.urls import path, include
from niicodeCo import views

urlpatterns = [
	path('', views.index, name= 'index'), 
    path('7545/', admin.site.urls),
    path('get/', include('niicodeCo.urls')),
]
