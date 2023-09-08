"""
URL configuration for ShppCar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from ventasApp.views import insertarProducto,eliminarEmpleado,ProductoDetail,clienteEdit,  eliminarCliente,ClienteDetail,  empleadoEdit,departamentoEdit,DepartamentoDetail,  ClienteListView,pedidoListView,insertarPedido, insertarCliente, productoEdit,createProductItem,productoListarView, insertProduct,delProd, inicio,ListarEmpleados,  RegistoEmpleadoLV, insertarRegEmpleado,  EmpleadoListView,EmpleadoDetail, ProductoListView, eliminarProducto, insertarDepartamento, DepartamentoListView, eliminarDepartamento, insertarEmpleado
from Shopping.views import tienda
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tienda),
    path('inicio',inicio,name='inicio'),
    path('createProduct', createProductItem.as_view()),
    path('verProducto', ProductoListView.as_view(), name='base-producto'),
    path('eliminarCliente/<int:cliente_no>', eliminarCliente),
    path('listarProdView', productoListarView.as_view()),
    path('verDepartamento', DepartamentoListView.as_view(), name='base-departamento'),
    path('verPedido', pedidoListView.as_view()),
    path('verCliente', ClienteListView.as_view(), name='base-cliente'),
    path('insertarCliente', insertarCliente),
    path('insertarPedido', insertarPedido),
    path('editarProducto/<pk>', productoEdit.as_view()),
    path('editarCliente/<pk>', clienteEdit.as_view()),
    path('editarEmpleado/<pk>', empleadoEdit.as_view()),
    path('editarDepartamento/<pk>', departamentoEdit.as_view()),
    path('mostrarRegEmpleado/<int:emp_no>', EmpleadoDetail.as_view()),
    path('mostrarCliente/<int:cliente_no>', ClienteDetail.as_view()),
    path('mostrarDepartamento/<int:depto_no>', DepartamentoDetail.as_view()),
    path('mostrarProducto/<int:producto_no>', ProductoDetail.as_view()),
    path('insertarRegEmpleado/<int:emp_no>', insertarRegEmpleado),
    path('verEmpleado', EmpleadoListView.as_view(), name='base-empleado'),
    path('eliminarProducto/<int:producto_no>', eliminarProducto),
    path('eliminarDepartamento/<int:depto_no>', eliminarDepartamento),
    path('eliminarEmpleado/<int:emp_no>', eliminarEmpleado),
    path('insertarProducto', insertarProducto),
    path('insertarDepartamento', insertarDepartamento),
    path('insertarEmpleado', insertarEmpleado),
    path('insertProd/<int:prodNum>', insertProduct),
    path('delProd/<int:prodNum>', delProd),
    path('listarEmpleados', ListarEmpleados),
    path('tienda/', include('Shopping.urls')),

    

    
    
]