from django.db import models
# para poder usar las relaciones entre tablas (autor (usuario) --> post)
from   django.contrib.auth.models import User

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'    

    def __str__(self) -> str:
        return self.nombre


#Clase correspondiente a las entradas del blog
class Post (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='blogs/' , null=True , blank= True)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'post'
        verbose_name_plural = 'posts'    

    def __str__(self) -> str:
        return self.titulo





