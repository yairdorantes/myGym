from django.contrib import admin
from django.urls import path
from .views import vistaregistros,acceso

urlpatterns = [
    path('formsreg/', vistaregistros.as_view(),name='formsreg'),
    #path()
    path('acceso/',acceso,name='acceso'),
]