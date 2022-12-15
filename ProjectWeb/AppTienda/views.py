from django.shortcuts import render, HttpResponse
from AppTienda.models import Categoria_producto , Producto

# Create your views here.

def tienda (request):
    #return HttpResponse("tienda")
    productos = Producto.objects.all()
    return render (request , 'AppTienda/tienda.html' , {'productos': productos}) 

'''
def categoria_producto (request, categoria_prodcuto_id) :
    categoria_producto = Categoria_producto.objects.get(id=categoria_prodcuto_id)
    producto = Producto.objects.filter(categoria_producto=categoria_producto)
    return render (request , 'AppTienda/categoria_producto.html' , 
    {'categoria_producto': categoria_producto , 'productos' : 'productos'})
'''

