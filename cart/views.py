from django.shortcuts import redirect, render
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart
from django.contrib import messages

@login_required(login_url='acceso')
def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    messages.success(request,'Producto agregado')
    return redirect('listproducts')

@login_required(login_url='acceso')
def add_product_two(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('carrito')


@login_required(login_url='acceso')
def remove_product(request, product_id):
    cart = Cart(request)
    producto = Product.objects.get(id=product_id)
    cart.remove(producto)
    return redirect('carrito')


@login_required(login_url='acceso')
def decrement_product(request, product_id):
    cart = Cart(request)
    producto = Product.objects.get(id=product_id)
    cart.decrement(product=producto)
    return redirect('carrito')


@login_required(login_url='acceso')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('carrito')


def show_cart(request):
    return render(request, 'cart/widget.html')

def show_product_(request,product_id):
    producto=Product.objects.get(pk=product_id)
    return render(request,'products/one_product.html',{
    'nombre':producto.name,'categoria':producto.name,
    'imagen':producto.image.url,'info':producto.detail,'precio':
    producto.price,'disponibilidad':producto.available
    })
