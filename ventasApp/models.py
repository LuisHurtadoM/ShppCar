from django.db import models

# Create your models here.
class Producto(models.Model):
    producto_no=models.PositiveSmallIntegerField(primary_key=True)
    descripcion=models.CharField(max_length=30,blank=False)
    precio_actual=models.FloatField()
    stock_disponible=models.FloatField()
    imagen=models.CharField(max_length=254,blank=False)
    

class Cliente(models.Model):
    cliente_no=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=30,blank=False)
    localidad=models.CharField(max_length=14,blank=False)
    vendedor_no=models.ForeignKey('Empleado',null=False,blank=False,on_delete=models.CASCADE)
    debe=models.DecimalField(max_digits=8,decimal_places=2)
    haber=models.DecimalField(max_digits=8,decimal_places=2)
    limite_credito=models.DecimalField(max_digits=8,decimal_places=2)

class Pedidos(models.Model):
    pedido_no = models.PositiveSmallIntegerField(primary_key=True)
    producto_no=models.ForeignKey('Producto',null=False,blank=False,on_delete=models.CASCADE)
    cliente_no=models.ForeignKey('Cliente',null=False,blank=False,on_delete=models.CASCADE)
    unidades=models.DecimalField(max_digits=8,decimal_places=0)
    fecha_pedidp=models.DateField

class Pedido(models.Model):
    pedido_no = models.PositiveSmallIntegerField(primary_key=True)
    producto_no=models.ForeignKey('Producto',null=False,blank=False,on_delete=models.CASCADE)
    cliente_no=models.ForeignKey('Cliente',null=False,blank=False,on_delete=models.CASCADE)
    unidades=models.DecimalField(max_digits=8,decimal_places=0)
    fecha_pedido=models.DateField()


class Vendedor(models.Model):
    vendedor_id=models.CharField(max_length=9,primary_key=True)
    vendedor_nombre=models.CharField(max_length=20,blank=False)
    vendedor_apellido=models.CharField(max_length=20,blank=False)
    vendedor_salario=models.DecimalField(max_digits=8,decimal_places=2)

class Departamento(models.Model):
    depto_no= models.PositiveSmallIntegerField(primary_key=True)
    dnombre=models.CharField(max_length=30,blank=False)
    localidad=models.CharField(max_length=30,blank=False)


class Empleado(models.Model):
    emp_no=models.PositiveSmallIntegerField(primary_key=True)
    apellido=models.CharField(max_length=30)
    oficio=models.CharField(max_length=30)
    director=models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_alta=models.DateField()
    salario=models.DecimalField(max_digits=8,decimal_places=2)
    comision=models.DecimalField(max_digits=8,decimal_places=2)
    depto_no = models.ForeignKey("Departamento",null=False,blank=False,on_delete=models.CASCADE)
    telefono=models.CharField(max_length=15)

class TiposRegistro(models.Model):
    tr_id = models.PositiveSmallIntegerField(primary_key=True)
    tr_descripcion = models.CharField(max_length=15, blank=False)

class RegistroEmpleado(models.Model):
    re_id = models.PositiveSmallIntegerField(primary_key=True)
    emp_no = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    re_fecha = models.DateField(auto_now_add=True)
    re_tipo = models.ForeignKey(TiposRegistro, null=False, on_delete=models.CASCADE)
    re_descripcion = models.CharField(max_length=800, blank=False)