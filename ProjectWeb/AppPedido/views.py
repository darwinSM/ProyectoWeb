from django.shortcuts import render , redirect
# decorador --> La app debe permitir hacer pedidos solo si se esta logueado
from django.contrib.auth.decorators import login_required
from AppPedido.models import Pedido  , Linea_Pedido
from AppShopingCart.carrito import Carrito

from django.contrib import messages 
from django.template.loader import render_to_string

from django.utils.html import strip_tags   # omitir etiquetas de html en una variable

from django.core.mail import send_mail  #funcion de djando para envio de mails


# Create your views here.
@login_required(redirect_field_name='Iniciar_sesion')  # redireccionar al usuario en caso de no estar logeado
def procesar_pedido (request):
    
    # Cuando se llame la funcion se da de alta el pedido, (el paarametro es el usuario que da de alta el pedido)
    pedido = Pedido.objects.create (user=request.user)
    
    #para poder ver lo que hay en el pedido se debe recorrer los items de carrito para almacenarlos primero 
    # en la linea_pedido (nombre, cantidad de unidades), y para ello primero se debe crear un objeto tipo Carrito
    carrito = Carrito(request)

    # Posteriormente Se crea una lista "lineas_pedido" para almacenar los elementos del carrito
    lineas_pedido = list()
    
    # Un bucle for , nos permitira ver ( clave : valor ) de cada item
    for key, value in carrito.carrito.items():
        #Cada item encontrado en el bucle , se agrega a la lista
        lineas_pedido.append(Linea_Pedido(
            producto_id = key,
            cantidad = value["cantidad"] ,
            user = request.user ,
            pedido = pedido 
        ))

        # Los elementos de esa lista se deben llevar a la base de datos (db)
        # El metodo bulk_create , recibe como parametro la lista y equivale a  procesar en lote varios "insert into",
        # para gusrdarlos en la tabla "Linea_Pedido" 
        Linea_Pedido.objects.bulk_create(lineas_pedido)
        
        # Enviar un mail al usuario
        # Sera llamada de otra funcion 
        enviar_mail (
            pedido = pedido ,
            lineas_pedido = lineas_pedido ,
            nombre_usuario = request.user.username ,
            email_usuario = request.user.email 
        ) 

        # Mensaje de feedback para informar al usuario
        messages.success(request , 'El pedido se ha creado correctamente')
        
        #Redieccionar a la tienda
        return redirect ('Tienda')


# django documentacion funcion: send_mail
# Esta funcion debe estar predeterminada para rebibir un numero indeterminado de parametros, 
def enviar_mail (**kwargs):
    # variable para guardar el asunto del mail
    asunto = "informacion sobre tu pedido" ,
    
    # variable que almacena toda la informacion sobre el pedido y las lineas de pedido
    # argumentos (template, lo que hay qu renderizar , q en este caso es un diccionario, 
    # que recoje la info que llega del kwargs )
    # El template se crea en Apptienda / emails / pedido.html
    # Es el archivo que se le enviara por correo electronico a la persona q ha hecho el pedido

    mensaje = render_to_string ('emails/pedido.html' , {
        
        "pedido": kwargs.get("pedido") ,
        "lineas_pedido" : kwargs.get("lineas_pedido") ,
        "nombre_usuario" : kwargs.get("nombre_usuario") ,
        })

    # variable que ignore todos los caracteres de tipo etiqueta html que puedan haber en la variable,
    #  i,e que tengan alguna etiqueta <>
    mensaje_texto = strip_tags (mensaje)

    # Especificar de quien procede el email que le vamos a enviar al usuario que ha hecho el pedido
    from_email = "darwincorreopruebas@gmail.com"

    # Especificar en la variable "to" el email del destinatario 
    # to = kwargs.get("email_usuario") -- # DESACTIVAR TEMPORALEMTE , hasta tener mail validos en los usuarios
    to = "darunal2022@gmail.com"

    #Ahora se utiliza la fucnion send_mail
    send_mail(
        subject = asunto ,
        message = mensaje_texto ,
        from_email = from_email,
        recipient_list = [to] ,
        fail_silently = True ,
        html_message= mensaje
    )   
    
    # Forma rapida de send_mail --> send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)


    
    