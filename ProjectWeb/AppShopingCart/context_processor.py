# En este archivo se desarrolla el proceso para crear una variable numerica global
# que vaya almacenando el precio de los articulos (disponible para todo el proyecto) 
# Este archivo por convencion se llama "context_processor.py"

# * solucion para error - activar y desactivar la siguiente linea
#from .carrito import Carrito


def importe_total_carrito(request):
    total=0
    # * solucion para error - activar y desactivar la siguiente linea
   # carrito = Carrito(request)

    # primero se debe determinar que el usuario este autenticado
    if request.user.is_authenticated:                                   #Cambio temporal del codigmientras se crea sesion de inicio
        #for key, value in request.session["carrito"].items():
            #total = total + (float(value["precio"])*value["cantidad"])
            None
    else:
        for key, value in request.session["carrito"].items():
            #total = total + (float(value["precio"])*value["cantidad"])  --> ERROR, correccion en siguiente linea
            total = total + float(value["precio"])
    return {"importe_total_carrito" : total}

# para poder acceder desde cualquier parte del proyecto al return "importe_total_carrito",
# se debe registrar el archivo "context_processor" en settings


