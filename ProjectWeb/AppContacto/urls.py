from django.urls import path
from AppContacto import views

urlpatterns = [
    path ('contacto/' , views.contacto, name='Contacto'),
]
