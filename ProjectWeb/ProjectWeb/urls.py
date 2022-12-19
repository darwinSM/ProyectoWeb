"""ProjectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
#from django.conf import settings
#from django.conf.urls.static import static

#from AppWeb import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppWeb/' , include('AppWeb.urls')) ,   # Enlace a la aplicacion de la urls de la aplicacion
    # si dejamos vacio el primer parametro del path '' --> En la direccion de la url se omite en la direccion de la ur  'AppWeb/'
    
    path ('AppServicios/' , include ('AppServicios.urls')),
    path ('AppBlog/' , include ('AppBlog.urls')),
    path ('AppContacto/' , include ('AppContacto.urls')),
    path ('AppTienda/' , include ('AppTienda.urls')),
    path ('AppShopingCart/' , include ('AppShopingCart.urls')),
    path ('AppAuth/' , include ('AppAuth.urls')) ,
    path ('AppPedido/' , include ('AppPedido.urls'))
    #path('', views.home , name='Home'),
    #path('servicio/' , views.servicio , name='Servicios'),
    #path('tienda/', views.tienda , name='Tienda'),
    #path('blog/' , views.blog , name='Blog'),
    #path('contacto/', views.contacto , name='Contactos'),

] 
# static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)



#Se agrega la nueva url de los archivos estaticos
#                                           esta es la raiz
urlpatterns+=static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)
