from django.shortcuts import render,redirect
from ..CuentaBancaria.models import *
from ..CuentaBancaria.views import *
from .models import *
from .carrito import carro
# Create your views here.

def compramenu(request):
    cuentas=filtraEstadosCuenta()
    return render(request,'cotizacion.html',{'cuenta':cuentas})

def pagar(request):
    id_ct=int(request.POST['id_cta'])
    print('cuentaid',id_ct)
    num=int(request.POST['num'])
    i=1
    while (i<=num):
        postdes='descrip'+str(i)     
        postcan='cant'+str(i)
        postpr='costoUnit'+str(i)
        postip='tipo'+str(i)
        print('------------------------------')
        descrip=request.POST[postdes]
        print('descripcion',descrip)
        cant=int(request.POST[postcan])
        print('cantidad',cant)
        precioUnit=float(request.POST[postpr])
        print('precio',precioUnit)
        tip=request.POST[postip]
        print('tipo',tip)
        print('------------------------------')
        i=i+1
        tran=compra.objects.create(descripcion=descrip,cantidad=cant,precio_unitario=precioUnit,tipo=tip,id_cuenta=cuenta.objects.get(id_c=id_ct))
    return redirect('/compra')

def agregar_prod(request,producto_id):
    Carro=carro(request)
    carro.agregar(producto=producto_id)
    
