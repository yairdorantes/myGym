from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View 
# Create your views here.
#from django.db import models
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render
from .forms import UserCreateForm

from django.contrib.auth.forms import AuthenticationForm


def acceso(request):
    #cart=Cart(request)
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            usuario = authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,f'Bienvenid@ de nuevo! {nombre_usuario}')
                return redirect('prueba')

            else:
                messages.error(request,'Los datos son incorrectos')
        else:
            messages.error(request,'Los datos son incorrectos')
    form = AuthenticationForm
    return render(request,'forms/auntenticacion.html',{'form':form})

class vistaregistros(View):
    #cart=Cart(request)
    def get(self,request):
        form = UserCreateForm()
        return render(request,'forms/forms.html',{'form':form})
    def post(self,request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_user = form.cleaned_data.get('username')
            messages.success(request,f'Bienvenid@ {nombre_user}')
            login(request,usuario)
            return redirect('prueba')
           
        else:
            #for i in form.error_messages:
            #    messages.error(request, form.error_messages[i])
            return render(request,'forms/forms.html',{'form':form})
'''      
def salir(request):
    logout(request)
    messages.success(request, F"Tu sesion se ha cerrado correctamente")
    return redirect('acceder')
'''