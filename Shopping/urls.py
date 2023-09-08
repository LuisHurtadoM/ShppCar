from Shopping.views import tienda, agregar_producto,sacar_producto,elimiar_carrito
from django.urls import path

urlpatterns = [
    
    path('', tienda, name='tienda'),
    path('agregar/<int:prod_id>', agregar_producto, name='agregar'),
    path('sacar/<int:prod_id>', sacar_producto, name='sacar'),
    path('limpiar/', elimiar_carrito, name='limpiar'),
]