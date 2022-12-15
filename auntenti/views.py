from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth import  logout






def salir(request):
    cart=Cart(request)
    logout(request)
    messages.success(request, F"Tu sesion se ha cerrado correctamente")
    return redirect('acceso')
