from django.db import models

# Create your models here.
from django.db import models

# Importamos la clase get_user.model
# Esta clase nos va a devlver el usuario actual (ususario logueado) 
from django.contrib.auth import get_user_model
from AppTienda.models import Producto            # Se importa la clase Producto de AppTienda
from django.db.models import F, Sum, FloatField  # Funciones importadas de dB para hacer operaciones y calcular el Total de una orden de pedido
                                    

# Create your models here.

# variable creada para poder usarla en la clase y acceder al usuario atual
User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Especificar el nombre para regristrar la tabla en la base de datos
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        # ordernar por id
        ordering = ['id']

    def __str__(self) -> str:
        return self.id

    
    # Como es necesario que la clase retorne el total del pedido (suma)
    # se debera agregar una propiedad en la clase, la propiedad "total"
    # Es neceario entonces usar el decorador @property

    @property
    def total(self):
        #pass       #pedido desgrosado
        return self.linea_pedido_set.aggregate(
            total = Sum (F('precio') * F('cantidad'), output_field = FloatField())
        )
        ["total"]


class Linea_Pedido (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        # Especificar el nombre para regristrar la tabla en la base de datos
        db_table = 'lineapedidos'
        verbose_name = 'linea_pedido'
        verbose_name_plural = 'lineas_pedido'

    def __str__(self) -> str:
        return f'{self.cantidad} unidades de {self.producto.nombre_producto}'



