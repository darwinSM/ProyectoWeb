# urls.py de la aplicacion AppWeb
from django.urls import path
from AppWeb import views

#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    
    path('home/', views.home , name='Home'),
    #path('servicio/' , views.servicio , name='Servicio'),
    path('tienda/', views.tienda , name='Tienda'),
    #path('blog/' , views.blog , name='Blog'),
    #path('contacto/', views.contacto , name='Contacto'),

]

#Se agrega la nueva url de los archivos estaticos
#                                           esta es la raiz
#urlpatterns+=static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)