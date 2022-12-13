from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from AppContacto.forms import FormularioContacto
#Importaciones para envio de email
from django.core.mail import EmailMessage

# Create your views here.

def contacto (request):
    #instanciar (crear una variable de la clase crada en views)
    formulario_contacto = FormularioContacto()
    
    # rescatar la infomacion cargada en el fornuario
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data = request.POST)   

        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
         
            email_enviado = EmailMessage(subject="mensaje desde app dJango",
                                body="El usuario {} con direccion {} envia el siguiente mensaje: \n\n {}".format(nombre,email,contenido),
                                from_email="",
                                to=["darunal2022@gmail.com"],
                                reply_to=[email])


            try: 
                email_enviado.send()
                #despues de haber hecho click en enviar (POST), se produce una recarga de la pagina (GET) se requere
                # redireccionar a contacto.html pasado un parametro en la recarga, ponga un mensaje en pantalla
                return redirect("/AppContacto/contacto/?valido")                # El parametro "valido", puede ser cualquier palabra de confirmacion
            
            except :
                return redirect("/AppContacto/contacto/?Novalido") 

    
    return render (request , 'AppContacto/contacto.html' , {'mi_formulario': formulario_contacto})



"""
def contacto (request):
    if request.method == 'POST' :
        form = FormularioContacto(request.POST)

        if form.is_valid():
            return HttpResponseRedirect ('/thanks/')
        else:  
            form = FormularioContacto()

    return render (request , 'AppContacto/contacto.html' , {'form':form})
"""

    


