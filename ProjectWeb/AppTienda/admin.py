from django.contrib import admin
from AppTienda.models import Categoria_producto , Producto


class Categoria_producto_Admin (admin.ModelAdmin):
    readonly_fields = ['created' , 'updated' ,]   #Los campos created y updated son de solo lectuta

class Producto_Admin (admin.ModelAdmin):
    readonly_fields = ['created' , 'updated']     #Los campos created y updated son de solo lectuta

# Register your models here.
admin.site.register(Categoria_producto , Categoria_producto_Admin)
admin.site.register(Producto , Producto_Admin)
