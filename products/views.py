
from django.shortcuts import render
from cart.cart import Cart
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from django.core.paginator import Paginator
def indexs(request):
    cart=Cart(request)
    listado_products=Product.objects.all()
    paginator=Paginator(listado_products,3)
    pagina=request.GET.get('page') or 1
    productos=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1,productos.paginator.num_pages+1)
    return render(request,'products/listado.html',{'productos':productos,'paginas':paginas,'pagina_actual':pagina_actual})

@login_required(login_url='acceso')
def listado_productos(request):
    cart = Cart(request)
    products=Product.objects.all()
    return render(request,'products/listado.html',{
        'products':products
    })

def show_product_(request,product_id):
    producto=Product.objects.get(pk=product_id)
    return render(request,'products/one_product.html',{
    'nombre':producto.name,'categoria':producto.category,
    'extracto':producto.excerpt,
    'imagen':producto.image.url,'info':producto.detail,'precio':
    producto.price,'disponibilidad':producto.available,'id':producto.id
    })
