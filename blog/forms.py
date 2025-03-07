from django import forms
from .models import Autor, Categoria, Post


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria', 'imagen']


class BusquedaPostForm(forms.Form):
    query = forms.CharField(label='Buscar Posts', max_length=100)