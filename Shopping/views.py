from django.shortcuts import render, redirect
from ventasApp.models import Producto
from .shpCar import Carrito
from django.http import HttpResponseRedirect, Http404
# Create your views here.
def tienda(request):
    productos=Producto.objects.all()
    return render(request,'tienda.html', {'productos':productos})

def agregar_producto(request,prod_id):
    carrito=Carrito(request)
    producto = Producto.objects.get(producto_no=prod_id)
    carrito.agregar(producto)
    response = HttpResponseRedirect('/')
    """ response.set_cookie('show_success_modal', 'true')
    return response  """
    return redirect('tienda')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto = Producto.objects.get(producto_no=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def elimiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect('tienda')