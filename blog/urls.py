from django.urls import path
from . import views  
from .views import PostListView

urlpatterns = [
    path('', views.home, name='post_list'),
    path('about/', views.about, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
]
