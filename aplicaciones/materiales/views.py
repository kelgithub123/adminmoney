from django.shortcuts import render,redirect
from ..CuentaBancaria.models import *
from ..CuentaBancaria.views import *
from .models import *
from .carrito import carro
# Create your views here.


def compramenu(request):
    cuentas=filtraEstadosCuenta()
    bill=billetera.objects.get(id_b=7)
    bill.cap=filtrarestadoBilletera()
    return render(request,'cotizacion.html',{'cuenta':cuentas,'e':bill})

def filtrarestadoBilletera():
    efectiv=transaccion.objects.filter(id_bill=billetera.objects.get(id_b=7))
    suma=0
    retiros=0
    if(efectiv):
        for tr in efectiv:
            suma=tr.Abono+suma
        for ret in efectiv:
            retiros=ret.retiro+retiros    
    total=suma-retiros
    return total

def pagoTransaccion(request,id_ct,num):
    i=1
    while (i<=num):
        postdes='descrip'+str(i)     
        postcan='cant'+str(i)
        postpr='costoUnit'+str(i)
        postip='tipo'+str(i)
        print('------------------------------')
        descrip=request.POST[postdes]
        print('descripcion',descrip)
        cant=float(request.POST[postcan])
        print('cantidad',cant)
        precioUnit=float(request.POST[postpr])
        print('precio',precioUnit)
        tip=request.POST[postip]
        print('tipo',tip)
        print('------------------------------')
        monto=cant*precioUnit
        i=i+1
        trans=transaccion.objects.create(retiro=monto,descripcion="transac. compras/otros",id_c=cuenta.objects.get(id_c=id_ct))
        comp=compra.objects.create(descripcion=descrip,cantidad=cant,precio_unitario=precioUnit,tipo=tip,id_transaccion=transaccion.objects.get(id_t=trans.id_t))
    

def pagar(request):
    id_ct=int(request.POST['id_cta'])
    print('cuentaid',id_ct)
    num=int(request.POST['num'])
    if (id_ct < 7):
        pagoTransaccion(request,id_ct,num)
    else:
        pagarEfectivo(request,id_ct,num)
    return redirect('/compra')

def pagarEfectivo(request,id_ct,num):
    id_bi=int(request.POST['id_cta'])
    print('id_billetera',id_bi)
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
        monto=cant*precioUnit
        i=i+1
        trans=transaccion.objects.create(retiro=monto,descripcion="transac. compras/otros",id_bill=billetera.objects.get(id_b=id_bi))
        comp=compra.objects.create(descripcion=descrip,cantidad=cant,precio_unitario=precioUnit,tipo=tip,id_transaccion=transaccion.objects.get(id_t=trans.id_t))
    