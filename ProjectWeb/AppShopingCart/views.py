from django.shortcuts import render

from .carrito import Carrito
from AppTienda.models import Producto
# cada vez que se haga una funcion con el carrito, se debera redireccionar a la pagina de la tienda 
# para reflejar los canbios hechos en el carrito
from django.shortcuts import redirect


# Create your views here.
def agregar_producto (request, producto_id):
    #Instanciar el objeto (crear un objeto de la clase Carrito)
    carrito = Carrito(request)
    
    #obtener el producto que se va a agregar al carro
    producto = Producto.objects.get(id=producto_id)
    
    # agregar el producto al carrito
    carrito.agregar_producto(producto=producto)

    # redireccionar a la tienda 
    return redirect ("Tienda") # ********** (Me parece que es Tienda)


def eliminar_producto (request, producto_id):
    #Instanciar el objeto (crear un objeto de la clase Carrito)
    carrito = Carrito(request)
    
    #obtener el producto que se va a agregar al carro
    producto = Producto.objects.get(id=producto_id)
    
    # eliminar el producto al carrito
    carrito.eliminar_producto(producto=producto)

    # redireccionar a la tienda 
    return redirect ("Tienda") # ********** (Me parece que es Tienda)


def restar_producto (request, producto_id):
    #Instanciar el objeto (crear un objeto de la clase Carrito)
    carrito = Carrito(request)
    
    #obtener el producto que se va a agregar al carro
    producto = Producto.objects.get(id=producto_id)
    
    # restar el producto al carrito
    carrito.restar_producto(producto=producto)

    # redireccionar a la tienda 
    return redirect ("Tienda") # ********** (Me parece que es Tienda)


def limpiar_carrito (request, producto_id):
    #Instanciar el objeto (crear un objeto de la clase Carrito)
    carrito = Carrito(request)
    
    # limpiar el producto al carrito
    carrito.limpiar_carrito()

    # redireccionar a la tienda 
    return redirect ("Tienda") # ********** (Me parece que es Tienda)    