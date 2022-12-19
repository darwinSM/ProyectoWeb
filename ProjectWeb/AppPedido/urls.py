from django.urls import path
from AppPedido import views 

urlpatterns = [
    
    path ('pedido/' , views.procesar_pedido , name='Pedido' )
]
