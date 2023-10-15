from django.shortcuts import render
from boleta.models import Boleta
from pedido.models import pedido

#se toman las boletas del model Boleta para mostrar en la tabla  de boleta/listado-boletas
def listarBoletas(request):
    boletas = Boleta.objects.all
    data = {'boletas':boletas}
    return render(request,'boleta/listado-boletas.html', data)
#saca la id de la url y se toma la coincidencia en el modelo para luego ir  a la pagina del detalle
def detalleBoleta(request):
   id_boleta = request.GET.get('id')
   print(id_boleta)
   boleta = Boleta.objects.get(id=id_boleta)
   print(boleta.__str__())
   data = {'boleta':boleta}
   return render(request, 'boleta/mostrar-boleta.html', data)
   