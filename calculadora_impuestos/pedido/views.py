from django.shortcuts import render
from django.http import HttpResponseRedirect
from pedido import models
from calculadora import views as views_calculadora


def crear_formulario(request):
    if request.method == "POST":
        print(request.POST)
    return render(request,"pedido/formulario.html")

#se guarda el pedido como objeto del modelo pedido
def guardar_pedido(request):
    if request.method == "POST":
        unidades =  request.POST.get('cantidadUnidades', '')
        costoDolar = request.POST.get('costoDolar','')
        nombreArticulo = request.POST.get('nombreArticulo', '')
        codigoArticulo = request.POST.get('codigoArticulo', '')
        nombreProveedor = request.POST.get('nombreProveedor', '')
        costoEnvio = request.POST.get('costoEnvio','')
        pedido = models.pedido.objects.create(cantidad_unidades=unidades,costo_unidad_dolar=costoDolar,nombre_articulo=nombreArticulo,codigo_articulo=codigoArticulo,nombre_proveedor=nombreProveedor, costo_envio=costoEnvio)
        #pedido.save()
        print(pedido.__dict__)
        print(request.POST)
        boleta = views_calculadora.calcular(pedido)
        return HttpResponseRedirect('/boleta/mostrarBoleta?id='+str(boleta.id))
        #return HttpResponseRedirect("/calcular", pedido)
    return HttpResponseRedirect("/pedido/formulario")
