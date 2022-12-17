from django.shortcuts import render, redirect           # redirect --> metodo para redirecionar
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm   # Importar clase UserCreationForm para crear el formulario de registro
from django.contrib.auth.forms import AuthenticationForm # Importar clase AuthenticationForm para crear el formulario de login
from django.contrib.auth import login, logout, authenticate         # Importar para usar metodo login, logout , y authenticate
from django.contrib import messages                      # Para mostrar mensajes de error en el diligenciamiento del formulario


# Create your views here.
class Registro(View):
    # Metodo get --> crea el formulario (El metodo get es el que muestra el formulario, es el que renderiza el formulario)
    def get(self, request):
        # Por convencion la variable se llama "form"
        form = UserCreationForm()
        #return render (request , 'UserCreate/userCreate.html')
        return render (request , 'UserCreate/userCreate.html' , {"form" : form})




    # Metodo post --> Gestiona el envio los datos a travez del formulario hacia la base de datos
    # request --> todods los datos que lleva la peticion: usuario, constraseña, .. 
    def post(self , request):
        #pass

        #form --> variable que almacena el formulario con toda la informacion que el usuario haya introducido 
        # (usuario y contraseña)
        form= UserCreationForm(request.POST)

        if form.is_valid():
            # variable que almacena la informacion grabada del formulario en la base de datos (tabla auth)
            #  (contraseña va encriptada)
            usuario= form.save()

            #una vez que el usuario se ha registrado exitosamente, el usuario queda automaticamente logeado,
            #para ello es necesario importar el metodo login 
            login (request, usuario)

            # Posteriormente se hace una redireccion (a la ruta home)
            return redirect ("Home")

        else:
            #pass
            #Hay que recorrer todos los mensajes de error q haya podido cometer el usuario
            for msg_error in form.error_messages :
                
                #mostrar cada mensaje de error en especifico del array de errores posibles
                messages.error (request, form.error_messages[msg_error])
                
                #Redireccionar al mismo formulario renderizado y dilegenciado (los campos correctos se cargan)
                #pero quedan en blanco los campos que se deben volver a diligenciar y se imprimen los mensajes de error
                return render (request , 'UserCreate/userCreate.html' , {"form":form})



# Fuera de la clase , se crea una vista para cerrar sesion
def cerrar_sesion (request):
    logout (request)
    return redirect ("Home")

# Vista para que un usuario registrado pueda iniciar sesion (loguearse)
def iniciar_sesion (request):
    #Si ha pulsado el boton login
    if request.method == "POST" :
        #Guarda en la variable form los datos que el usuario ha introducido en el formulario
        form = AuthenticationForm(request , data=request.POST)

        #Se valida el formulario
        if form.is_valid():
            #Se guarda en las variables , ol que le usuario ha digitado en los campos username y password
            nombre_usuario = form.cleaned_data.get("username")
            password_usuario = form.cleaned_data.get("password")

            # El metodo "authenticate" permite verificar si la informacion guaradada es igual a
            # la informacion de la base de datos
            
            # Se crea una variable que guarde la autenticacion
            usuario = authenticate(username = nombre_usuario , password = password_usuario)
            
            # si esa variable existe es porque la informacion rescatada es correspondiente, 
            # si la variable no existe es por que la info no fue correspondiente
            if usuario :
                login(request , usuario)
                return redirect ("Home")
            
            else:
                messages.error (request, "*** usuario no autorizado ***")  
            
        # Si el formulario no es valido, i,e, la informacion no fue introducida de forma correcta
        else:
            messages.error (request, " *** Error - Login incorrecto *** ") 

    # Si no hace clock en el boton login
    
    # para el metodo de autenticacion se utiliza la clase authenticationForm
    form = AuthenticationForm()
    return render (request , 'UserLogin/userLogin.html' , {"form" : form})

