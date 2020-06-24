from django.urls import path
from .views import Post, admin


urlpatterns = [
	path('blog/', Post, name='Post'),
	path('admin/', admin, name='admin'),

]