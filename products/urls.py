
from django.urls import path
from .views import indexs,show_product_
from products import views
urlpatterns=[
    path('listproducts/',indexs,name='listproducts'),
    path('product/<int:product_id>',show_product_,name='product'),
   
]
