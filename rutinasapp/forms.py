
from django import forms
from .models import Post
from django.contrib import messages
class formupost(forms.ModelForm):
    class Meta:
        model=Post
        fields=('categoria','titulo','contenido','imagen')

