from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    #return HttpResponse("home")
    return render (request, 'AppWeb/home.html')


def tienda (request):
    #return HttpResponse("tienda")
    return render (request , 'AppWeb/tienda.html')

# Esta vista se traslada a view de la AppBlog
'''
def blog (request):
    #return HttpResponse("blog")
    return render (request , 'AppWeb/blog.html')
'''

# Esta vista se traslada a view de la AppContacto
'''
def contacto (request):
    #return HttpResponse("contacto")
    return render (request ,'AppWeb/contacto.html')
'''