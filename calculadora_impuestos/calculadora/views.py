from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from pedido import models as models_pedido
from boleta import models as models_boleta
from decimal import *

# Create your views here.
def calcular(pedido):
    print(pedido.__dict__)
    total_pedido=int(pedido.cantidad_unidades)*(890*int(pedido.costo_unidad_dolar))
    costo_envio=(int(pedido.costo_envio))*890
    cif=Decimal(total_pedido+costo_envio)
    tasa_aduana= cif*Decimal(0.06)
    impuesto_iva=cif*Decimal(0.19)
    total_agregado=tasa_aduana+impuesto_iva
    total_compra_clp=cif+total_agregado+costo_envio
    total_compra_usd=int(total_compra_clp/890)
    calculo = models_boleta.Boleta.objects.create(total_pedido=total_pedido,costo_envio=costo_envio,tasa_aduana=tasa_aduana,impuesto_iva=impuesto_iva,total_agregado=total_agregado,total_compra_clp=total_compra_clp,total_compra_usd=total_compra_usd,id_pedido=pedido)
    return calculo