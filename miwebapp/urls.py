from django.contrib import admin
from django.urls import path
from miwebapp import views
from cart.views import show_cart
urlpatterns = [
    path('home/', views.home,name='home'),
    path('carrito/',show_cart,name='carrito'),
]
