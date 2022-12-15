
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from rutinasapp.forms import formupost
from django.contrib import messages
from rutinasapp.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
@login_required(login_url='acceso')

def indexs(request):
    cart=Cart(request)
    listado_post=Post.objects.all()
    paginator=Paginator(listado_post,3)
    pagina=request.GET.get('page') or 1
    posts=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    return render(request,'rutinasapp/prueba.html',{'posts':posts,'paginas':paginas,'pagina_actual':pagina_actual})
@login_required(login_url='acceso')    
def crear_post(request):
    
    if request.method=='POST':
        form=formupost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor_id=request.user.id
            post.save()
            titulo=form.cleaned_data.get('titulo')
            messages.success(request,f'El post {titulo} se ha creado correctamente')
            return redirect('prueba')
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))

    form=formupost()
    return render(request,'rutinasapp/crear_post.html',{'form':form})
@login_required(login_url='acceso')

def eliminar_post(request,post_id):
    
    try:
        post=Post.objects.get(pk=post_id)
    except post.DoesNotExist:
        messages.error(request,'EL post que quieres eliminar no existe')
        return redirect('prueba')
    if post.autor != request.user:
        messages.error(request,'No eres autor de este post')
        return redirect('prueba')
    post.delete()
    messages.success(request,f'El post {post.titulo} ha sido eliminado')
    return redirect('prueba')


def show_content(request,post_id):
    
    post=Post.objects.get(pk=post_id)
    return render(request,'rutinasapp/post.html',{'titulo':post.titulo,'imagen':post.imagen.url,'contenido':post.contenido,'autor':post.autor.username,'fecha':post.fecha_alta})



    

