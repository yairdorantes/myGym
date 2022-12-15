from django.contrib import admin
from django.urls import path
#from .views import vistaregistro
from .views import salir

urlpatterns = [
    path('salir/',salir, name='salir'),
]

