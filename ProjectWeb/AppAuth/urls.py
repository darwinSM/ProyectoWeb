from django.urls import path

# como la viesta ahoraes una clase, y no una funcion, entonces se modifica la importacion
# y se modifica el codigo de urlpatterns, para que muestre la clase, como una vista (as_view())

from .views import Registro 
from AppAuth import views


urlpatterns = [
    
    path('auth/', Registro.as_view() , name='Auth'),
    path('cerrar_sesion/' , views.cerrar_sesion , name="Cerrar_sesion") ,
    path('iniciar_sesion/' , views.iniciar_sesion , name='Iniciar_sesion') ,
  
]
