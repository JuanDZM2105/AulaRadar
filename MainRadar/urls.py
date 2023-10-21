
from django.urls import path
from .views import home,main,exit

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    path('logout/',exit, name='exit'),
    
]