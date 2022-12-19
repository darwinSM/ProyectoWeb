from django.contrib import admin
from AppPedido.models import Pedido , Linea_Pedido


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

class Linea_PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']  


# Register your models here.
admin.site.register (Pedido, PedidoAdmin)
admin.site.register (Linea_Pedido , Linea_PedidoAdmin)
