from django.shortcuts import render

from AppServicios.models import Servicio
# Create your views here.

def servicio(request):
    #return HttpResponse("servicio")
    servicios = Servicio.objects.all()      #variable que importa todos los objetos (servicios) dentro de la clase Servicios
    return render (request,'AppServicios/servicio.html' , {'servicios' : servicios})  #eL Tercer parametro Incluye en el render los serivios creados 
