from django.urls import path
from AppShopingCart import views

# Para poder acceder de una mejor forma las url, se le asigna un name:
# se le antepone al name de cada ruta (para evitar colision de rutas), ej: "carrito/Agregar" , "carrito/Eliminar" , ...
app_name = "carrito"

urlpatterns = [
       
    path('agregar/<int:producto_id>/' , views.agregar_producto , name='Agregar'),
    path('eliminar/<int:producto_id>/' , views.eliminar_producto , name='Eliminar'),
    path('restar/<int:producto_id>/' , views.restar_producto , name='Restar'),
    path('limpiar/' , views.limpiar_carrito, name='Limpiar'),
]