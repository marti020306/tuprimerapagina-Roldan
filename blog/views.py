from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post 
from .forms import BusquedaPostForm

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
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Post'})

def buscar_post(request):
    resultados = []
    no_resultados = False
    if request.method == "GET" and 'query' in request.GET:
        form = BusquedaPostForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Post.objects.filter(titulo__icontains=query)
            if not resultados:
                no_resultados = True
    else:
        form = BusquedaPostForm()
    return render(request, 'blog/busqueda.html', {'form': form, 'resultados': resultados, 'no_resultados': no_resultados})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'blog/post_form.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list') 

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_confirm_delete.html'

from django.shortcuts import render

def about(request):
    return render(request, 'blog/about.html')


