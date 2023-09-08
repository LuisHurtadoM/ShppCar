from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, Page
from ventasApp.models import Producto, Vendedor,Pedido, Departamento, Empleado, RegistroEmpleado, TiposRegistro, Cliente
from django.views.generic import ListView,DetailView, CreateView,UpdateView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy

# Create your views here.
def insertarProducto(request):
    var_producto_no=request.POST['producto_no']
    var_descripcion=request.POST['descripcion']
    var_precio_actual=request.POST['precio_actual']
    var_stock_disponible=request.POST['stock_disponible']
    var_imagen=request.POST['imagen']
    producto = Producto.objects.create(producto_no=var_producto_no,
                                   descripcion=var_descripcion,
                                   precio_actual=var_precio_actual,
                                   stock_disponible=var_stock_disponible,
                                   imagen=var_imagen)

    response = HttpResponseRedirect('/verProducto')
    response.set_cookie('show_success_modal', 'true')
    return response
   # return redirect('/verProducto')

def insertarCliente(request):
    var_cliente_no=request.POST['cliente_no']
    var_nombre=request.POST['nombre']
    var_localidad=request.POST['localidad']
    var_vendedor_no=request.POST['vendedor_no']
    var_debe=request.POST['debe']
    var_haber=request.POST['haber']
    var_limite_credito=request.POST['limite_credito']

    cliente = Cliente.objects.create(cliente_no = var_cliente_no,
                                     nombre=var_nombre,
                                     localidad=var_localidad,
                                     vendedor_no_id=var_vendedor_no,
                                     debe = var_debe,
                                     haber=var_haber,
                                     limite_credito = var_limite_credito)
    response = HttpResponseRedirect('/verCliente')
    response.set_cookie('show_success_modal', 'true')
    return response


def insertProduct(request,prodNum):
    product = Producto(producto_no= prodNum,
                       descripcion= 'inserto',
                       precio_actual=25,
                       stock_disponible=250,
                       )
    product.save()
    return redirect('/')

def delProd(request,prodNum):
    product= Producto(producto_no=prodNum)
    product.delete()
    return redirect('/')



def editarProducto(request, prodNum):
    # Obtén el producto a editar o muestra un error 404 si no existe
    producto = get_object_or_404(Producto, pk=prodNum)
    
    # Actualiza los atributos del producto con los nuevos valores
    producto.producto_no = request.POST['producto_no']
    producto.descripcion = request.POST['descripcion']
    producto.precio_actual = request.POST['precio_actual']
    producto.stock_disponible = request.POST['stock_disponible']

    # Guarda los cambios en la base de datos
    producto.save()

    response = HttpResponseRedirect('/verProducto')
    response.set_cookie('show_success_modal', 'true')
    return response



class createProductItem(CreateView):
    model = Producto
    fields=["producto_no","descripcion","precio_actual", "stock_disponible"]
    success_url=reverse_lazy('base-producto')
    
class productoListarView(ListView):
    model = Producto
    template_name='datos.html'
    def get_queryset(self):
        return Producto.objects.all()

class productoEdit(UpdateView):
    model=Producto
    fields=["descripcion","precio_actual","imagen", "stock_disponible"]
    success_url=reverse_lazy('base-producto')

class departamentoEdit(UpdateView):
    model=Departamento
    fields=["dnombre","localidad"]
    success_url=reverse_lazy('base-departamento')

class empleadoEdit(UpdateView):
    model = Empleado
    fields=["apellido","salario","oficio"]
    success_url=reverse_lazy('base-empleado')

class clienteEdit(UpdateView):
    model = Cliente
    fields=["nombre","localidad","debe","haber","limite_credito"]
    success_url=reverse_lazy('base-empleado')

def insertarEmpleado(request):
    
    var_emp_no=request.POST['emp_no'] 
    var_apellido=request.POST['apellido']
    var_oficio=request.POST['oficio']
    var_director=request.POST['director']
    var_fecha_alta=request.POST['fecha_alta']
    var_salario=request.POST['salario']
    var_comision=request.POST['comision']
    var_depto_no=request.POST['depto_no']
    var_telefono=request.POST['telefono']

    
    director_emp=Empleado.objects.get(emp_no=var_director)
    empleado=Empleado.objects.create(emp_no=var_emp_no,
                                      apellido=var_apellido,
                                      oficio=var_oficio,
                                      director_id=director_emp.emp_no,
                                      fecha_alta=var_fecha_alta,
                                      salario=var_salario,
                                      comision=var_comision,
                                      depto_no_id=var_depto_no,
                                      telefono=var_telefono)
    
    
    response = HttpResponseRedirect('/verEmpleado')
    response.set_cookie('show_success_modal', 'true')
    return response
    #return redirect('/verEmpleado')

def insertVendedor(request):
    var_venededor_id= request.POST['vendedor_id']
    var_vendedor_nombre=request.POST['vendedor_nombre']
    var_vendedor_apellido= request.POST['vendedor_apellido']
    var_vendedor_salario=request.POST['vendedor_salario']
    
    vendedor = Vendedor.objects.create(vendedor_id=var_venededor_id,
                                       vendedor_nombre=var_vendedor_nombre,
                                       vendedor_apellido=var_vendedor_apellido,
                                       vendedor_salario=var_vendedor_salario)
    return redirect('/verVendedor')

def inicio(request):
    return render(request,'index.html')
    



def insertarDepartamento(request):
    var_depto_no=request.POST['depto_no']
    var_dnombre= request.POST['dnombre']
    var_localidad=request.POST['localidad']
    
    departamento = Departamento.objects.create(depto_no=var_depto_no,
                                               dnombre=var_dnombre,
                                               localidad=var_localidad)
    
    response = HttpResponseRedirect('/verDepartamento')
    response.set_cookie('show_success_modal', 'true')
    return response
    #return redirect('/verDepartamento')

def insertarPedido(request):
    var_pedido_no=request.POST['pedido_no']
    var_producto_no= request.POST['producto_no']
    var_cliente_no=request.POST['cliente_no']
    var_unidades=request.POST['unidades']
    var_fecha_pedido=request.POST['fecha_pedido']

    pedido = Pedido.objects.create(pedido_no=var_pedido_no,
                                    producto_no_id=var_producto_no,
                                    cliente_no_id=var_cliente_no,
                                    unidades=var_unidades,
                                    fecha_pedido=var_fecha_pedido)
    
    response = HttpResponseRedirect('/verPedido')
    response.set_cookie('show_success_modal', 'true')
    return response


class pedidoListView(ListView):
    model=Pedido
    template_name='pedido.html'
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["client"] = Cliente.objects.all()
        contexto["prod"] = Producto.objects.all()
        return contexto
    def get_queryset(self):
        return Pedido.objects.all()    



def insertarRegEmpleado(request,emp_no):
    
    var_re_tipo=request.POST['treg_id']
    var_re_fecha=request.POST['re_fecha']
    var_re_descripcion=request.POST['tr_descripcion']

    var_re_t=TiposRegistro.objects.get(tr_id=var_re_tipo)
    registroEmpleado = RegistroEmpleado.objects.create(emp_no_id=emp_no,
                                                       re_tipo_id=var_re_t,
                                                       re_fecha=var_re_fecha,
                                                       re_descripcion=var_re_descripcion)
    return redirect('/verEmpleado')



class DepartamentoListView(ListView):
    model = Departamento
    template_name= 'depto.html'
    def get_queryset(self):
        return Departamento.objects.all()


class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado.html'
    def get_queryset(self):
        return Empleado.objects.all()
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["deps"] = Departamento.objects.all()
        return contexto

    
    

class ClienteListView(ListView):
    model = Empleado
    template_name = 'cliente.html'
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["emp"] = Empleado.objects.all()
        return contexto

    def get_queryset(self):
        return Cliente.objects.all()

def ListarEmpleados(request):
    empleados = Empleado.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(empleados, 10)  
    try:
        empleados = paginator.page(page)
    except:
        raise Http404

    data = {
        'empleados': empleados
    }

    return render(request, 'C:/Users/Luis/api/ventasApp/templates/empleado2.html', data)




class RegistoEmpleadoLV(ListView):
    model=RegistroEmpleado
    template_name='insertarRegEmp.html'
    def get_context_data(self,**kwargs):
        context2=super().get_context_data(**kwargs)
        context2["regis"]=TiposRegistro.objects.all()
        return context2
    def get_object(self):
        myobject=self.model.objects.get(emp_no=self.kwargs['emp_no'])
        return myobject

class EmpleadoDetail(DetailView):
    model=Empleado
    template_name='empleadoDetail.html'
    def get_context_data(self,**kwargs):
        context2=super().get_context_data(**kwargs)
        context2["regis"]=RegistroEmpleado.objects.filter(emp_no=self.kwargs['emp_no'])
        return context2
        
    
    def get_object(self):
        myobject=self.model.objects.get(emp_no=self.kwargs['emp_no'])
        return myobject


class DepartamentoDetail(DetailView):
    model=Departamento
    template_name='deptoDetail.html'
        
    
    def get_object(self):
        myobject=self.model.objects.get(depto_no=self.kwargs['depto_no'])
        return myobject

class ClienteDetail(DetailView):
    model=Cliente
    template_name='clienteDetail.html'
        
    
    def get_object(self):
        myobject=self.model.objects.get(cliente_no=self.kwargs['cliente_no'])
        return myobject






class ProductoDetail(DetailView):
    model=Producto
    template_name='datosDetail.html'
        
    
    def get_object(self):
        myobject=self.model.objects.get(producto_no=self.kwargs['producto_no'])
        return myobject

class VendedorListView(ListView):
    model = Vendedor
    template_name='vendedores.html'
    def get_queryset(self):
        return Vendedor.objects.all()
    
class ProductoListView(ListView):
    model= Producto
    template_name='datos.html'
    def get_queryset(self):
        return Producto.objects.all()


def eliminarProducto(request,producto_no):
    producto=Producto.objects.get(producto_no=producto_no)
    response = HttpResponseRedirect('/verProducto')
    response.set_cookie('show_success_del', 'true')
    producto.delete()
    return response



def eliminarCliente(request,cliente_no):
    producto=Cliente.objects.get(cliente_no=cliente_no)
    response = HttpResponseRedirect('/verCliente')
    response.set_cookie('show_success_del', 'true')
    producto.delete()
    return response

def eliminarEmpleado(request,emp_no):
    empleado=Empleado.objects.get(emp_no=emp_no)
    response = HttpResponseRedirect('/verEmpleado')
    response.set_cookie('show_success_del', 'true')
    empleado.delete()
    return response


def eliminarDepartamento(request,depto_no):
    departamento=Departamento.objects.get(depto_no=depto_no)
    response = HttpResponseRedirect('/verDepartamento')
    response.set_cookie('show_success_del', 'true')
    departamento.delete()
    return response
