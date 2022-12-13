from django.db import models

# Create your models here.

class Servicio (models.Model):
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios/')  #parametro upload_to = "directorio donde se suben las imagenes"
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self) -> str:
        return self.titulo


