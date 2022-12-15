

from django.urls import path
from .views import add_product,remove_product,decrement_product,clear_cart,add_product_two,show_product_
app_name = "cart" 
urlpatterns = [
    path('add_product/<int:product_id>/',add_product,name='add_product'),
    path('remove_product/<int:product_id>/',remove_product,name='remove_product'),
    path('decrement_product/<int:product_id>/',decrement_product,name='decrement_product'),
    path('clear/',clear_cart,name='clear_cart'),
    path('add_product_two/<int:product_id>/',add_product_two,name='add_product_two'),
    path('product/<int:product_id>',show_product_,name='product'),
]
