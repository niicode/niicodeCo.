from django.contrib import admin
from django.urls import path, include
from niicodeCo import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('7545/', admin.site.urls),
    path('niicode/', include('niicodeCo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
