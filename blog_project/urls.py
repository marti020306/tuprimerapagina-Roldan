"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('accounts/', include('accounts.urls')),
    path('about/', include('blog.urls')),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    


