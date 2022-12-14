from django.urls import path
from AppTienda import views

urlpatterns = [
       
    path('tienda/' , views.tienda , name='Tienda'),
    
]