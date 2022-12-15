
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

#from markdownx.models import markdownx

# Create your models here.
from django import template


class categoria(models.Model):
    nombre=models.CharField(max_length=100,null=False,unique=False,verbose_name='Nombre')
    
    class meta:
        verbose_name='Categoria'
        ordering=['id']
    def __str__(self):
        return self.nombre
class Post(models.Model):  
    autor=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=100,unique=True,null=False,verbose_name='Titulo')
    contenido=models.TextField(null=True,verbose_name='Contenido post')
    imagen=models.ImageField(upload_to='rutinas',null=False,blank=False,verbose_name='imagen post')
    fecha_alta=models.DateTimeField(auto_now_add=True,verbose_name='Fecha alta')
    fecha_actualizacion=models.DateTimeField(auto_now_add=True,verbose_name='Fecha actualizacion')
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args,**kwargs)
    def __str__(self):
        return self.titulo
    class meta:
        db_table='posts'
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering=['id']
