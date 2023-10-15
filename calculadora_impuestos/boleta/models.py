from django.db import models
from pedido.models import pedido

# se crea un modelo de los calculos del pedido
class Boleta(models.Model):
    total_pedido = models.PositiveIntegerField()
    costo_envio = models.PositiveIntegerField()
    tasa_aduana = models.PositiveIntegerField()
    impuesto_iva = models.PositiveIntegerField()
    total_agregado = models.PositiveIntegerField()
    total_compra_clp = models.PositiveIntegerField()
    total_compra_usd = models.PositiveIntegerField()
    id_pedido = models.ForeignKey(pedido , on_delete=models.CASCADE)

