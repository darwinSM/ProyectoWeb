from django.urls import path
from AppServicios import views

urlpatterns = [
       
    path('servicio/' , views.servicio , name='Servicio'),
    
]