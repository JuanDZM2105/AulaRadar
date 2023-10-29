
from django.urls import path
from .views import home,main,exit,more_info

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    path('logout/',exit, name='exit'),
     path('main/more_info/<int:id_unico>/', more_info, name='more_info'),
    
]