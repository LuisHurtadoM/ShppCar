from ventasApp.models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            self.session['carrito'] = {}
            self.carrito=self.session['carrito']
        else:
            self.carrito = self.session['carrito']

    def agregar(self, producto):
        id = str(producto.producto_no)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_no': producto.producto_no,
                'nombre': producto.descripcion,
                'precio': producto.precio_actual,
                'cantidad': 1,
                'subtotal': producto.precio_actual
            }
        else:
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['subtotal'] += producto.precio_actual
        self.guardar_carrito()

    def sacar(self, producto):
        id = str(producto.producto_no)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['subtotal'] -= producto.precio_actual
            if self.carrito[id]['cantidad']==0:
                del self.carrito[id]
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True
