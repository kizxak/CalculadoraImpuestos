"""
URL configuration for calculadora_impuestos project.

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
from django.urls import path
from django.shortcuts import redirect
from boleta import views as views_boleta
from pedido import views as views_pedido
from calculadora import views as views_calculadora

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('listarBoletas')),
    path('boleta/listarBoletas', views_boleta.listarBoletas, name='listarBoletas'),
    path('pedido/formulario', views_pedido.crear_formulario),
    path('pedido/guardarPedido', views_pedido.guardar_pedido),
    path('calcular', views_calculadora.calcular),
    path('boleta/mostrarBoleta', views_boleta.detalleBoleta)
    
]
