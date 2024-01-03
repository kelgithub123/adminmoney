from django.shortcuts import render,redirect
from .models import cuenta,transaccion
from ..materiales.models import *
# Create your views here.
def menuRegcuenta(request):    
    return render(request,"registroCuenta.html")

def registrarcuenta(request):
    ban= request.POST['banco']
    cap=request.POST['capital']
    tip=request.POST['tipoDcuenta']
    inter=request.POST['interes']
    fec=request.POST['fecha']
    cuentas = cuenta.objects.create(banco=ban,capital=cap,tipo=tip,interes=inter,fecha=fec)
    return redirect('/')

def filtraEstadosCuenta():
    cuentas=cuenta.objects.all()
    listcuentas=[]
    for ct in cuentas:
        totalr=totalretiros(ct.id_c)
        totala=totalabonos(ct.id_c)
        ct.capital=ct.capital+totala-totalr
        ct.capini=ct.capital+totala+totalr
        ct.retiros=totalr
        ct.abonos=totala
        listcuentas.append(ct)
    return listcuentas

def listaDecuentas(request):
    ctafil=filtraEstadosCuenta
    return render(request,"ListaDcuentas.html",{"cuentas":ctafil})

def retirar(request,idcta):
    monto=request.POST['num']
    trans=transaccion.objects.create(retiro=monto,id_c=cuenta.objects.get(id_c=idcta))
    return redirect('/cuentas')

def totalretiros(id):
    saldo=transaccion.objects.filter(id_c=id)
    Compras=compra.objects.filter(id_cuenta=id)
    totalRetiros=0
    totcompras=0
    if (saldo):
        for s in saldo:
            totalRetiros=s.retiro+totalRetiros
    if (Compras):    
        for c in Compras:
            totcompras=(c.cantidad*c.precio_unitario)+totcompras
    total=totcompras+totalRetiros;        
    return total

def totalabonos(id):
    saldo=transaccion.objects.filter(id_c=id)
    total=0
    if (saldo):
        for s in saldo:
            total=s.Abono+total
    return total