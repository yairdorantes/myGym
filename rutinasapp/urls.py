
from django.contrib import admin
from django.urls import path
from .views import crear_post,indexs,eliminar_post,show_content

urlpatterns = [
    path('prueba/',indexs,name='prueba'),   
    path('crearpost/',crear_post,name='crear_post'), 
    path('eliminarpost/<int:post_id>',eliminar_post,name='eliminarpost'),
    path('showpost/<int:post_id>',show_content,name='show_post')
]

