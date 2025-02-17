from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm # type: ignore

def home(request):
    return render(request, 'blog/base.html')

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Autor'})

def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Categoría'})

def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Post'})

def buscar_post(request):
    resultados = []
    if request.method == "GET" and 'query' in request.GET:
        form = BusquedaPostForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Post.objects.filter(titulo__icontains=query)
    else:
        form = BusquedaPostForm()
    return render(request, 'blog/busqueda.html', {'form': form, 'resultados': resultados})
