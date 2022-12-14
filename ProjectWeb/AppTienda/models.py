from django.db import models

# Create your models here.
class Categoria_producto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'Categoria_prodcuto'
        verbose_name_plural = 'Categoria_productos'

    def __str__(self) -> str:
        return self.nombre

class Producto (models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField(default=0, null=False)
    #cantidad =models.IntegerField(default=0,null=False) 
    imagen = models.ImageField(upload_to='tienda/' , null=True , blank= True)
    disponibilidad = models.BooleanField(default=True)

    categoria_producto = models.ForeignKey(Categoria_producto, 
                        on_delete=models.DO_NOTHING, null=False,
                        blank=False,related_name="Categoria_producto")

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'producto'
        verbose_name_plural = 'productos'    
    

    def __str__(self) -> str:
        return self.nombre_producto 