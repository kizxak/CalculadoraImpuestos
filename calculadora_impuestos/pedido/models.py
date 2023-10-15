from django.db import models

# Se crea un modelo del pedido ingresado por el usuario
class pedido(models.Model):
    cantidad_unidades=models.PositiveIntegerField()
    costo_unidad_dolar=models.PositiveIntegerField()
    nombre_articulo=models.CharField(max_length=250)
    codigo_articulo=models.PositiveIntegerField()
    nombre_proveedor=models.CharField(max_length=50)
    costo_envio=models.PositiveIntegerField()
    
    