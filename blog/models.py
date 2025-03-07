from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.conf import settings 

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_blog/', blank=True, null=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) 
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})