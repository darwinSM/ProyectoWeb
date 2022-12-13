from django.contrib import admin
from AppServicios.models import Servicio   # Importamos los modelos desde la app


# para que en el panel de admnistracion aparezcan los campos created y updated -»
class ServicioAdmin(admin.ModelAdmin):
    
    readonly_fields = ['created', 'updated',]


# Register your models here.
#Deben ir registrados en la misma fila
admin.site.register(Servicio, ServicioAdmin)

