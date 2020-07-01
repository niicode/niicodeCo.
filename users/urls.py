from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
