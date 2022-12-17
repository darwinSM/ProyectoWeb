#Esta clase estara encargada de realizar todas las taeas asignadas al carrito de compras
# 1. Manejo de seson
# 2. agregar productos
# 3. eliminar productos
# 4. restar cantidad de productos
# 5. vaciar carrito 

class Carrito: 
    #contructor
    def __init__(self, request):
        
        #almacenar la peticion actual para utilizarla despues dentro de esta misma clase
        self.request = request

        #de la misma forma con la sesion
        self.session = request.session

        #construir un carrito de compras para esta sesion (igualar la sesion del ususario con el carrito)
        carrito = self.session.get("carrito")
        
        #El carro es un diccionario que almacena productos, con su clave (id) y su respectivo valor (el valor es
        # otro diccionario con las caacteristicas del producto) {id1:{nombre:XX1 , precio:yy1}, id2:{nombre2:xx2 , precio2:yy2}}
        if not carrito:
            carrito = self.session["carrito"]={}
        #si ya hay carro entonces
        #else :
        
        #carrito = Carrito(request)
        self.carrito = carrito

    #funcion para agregar productos
    def agregar_producto (self , producto) :
        #se agrega un producto si no esta previamente en el carro, lo agrega por primera vez
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "producto_id" : producto.id,
                "nombre_producto" : producto.nombre_producto ,
                "precio" : str(producto.precio),
                "cantidad" : 1 ,
                "imagen" : producto.imagen.url 
            }
        #En caso de que el carro ya tenga un producto igual, entonces que agregue otra unidad
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"]=producto.precio * value["cantidad"]
                    #value['precio'] = int (value['precio']) + producto.precio   #codigo del profe
                    break

        # Actualizar la sesion, con los nuevos datos de el carrito 
        self.guardar_carrito ()

    def guardar_carrito (self):
        self.session ["carrito"] =self.carrito
        self.session.modified = True


    #Eliminar un producto (COn todas las unidades relacionadas a el)
    def eliminar_producto (self , producto):
        producto.id =str(producto.id)

        if producto.id in self.carrito:
            #del --> funcion eliminar
            del self.carrito[producto.id]
            self.guardar_carrito()

    # restar uniades de un productos en elcarrito
    def restar_producto (self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] - 1
                    value["precio"]=producto.precio * value["cantidad"]
                    # value['precio'] = int (value['precio']) - producto.precio   # codigo del profe
                   
                    # Si se restan todas las unidades del producto, entoces se debe eliminar el producto
                    if value["cantidad"] < 1:
                        self.eliminar_producto(producto)
                    break
        self.guardar_carrito()


    #funcion para vaciar todo el carrito
    def limpiar_carrito (self):
        self.session["carrito"] = {}
        self.session.modified = True






        
