from django.shortcuts import render,redirect
from .models import *
from ..materiales.models import *
import datetime
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
    trans=transaccion.objects.create(retiro=monto,fecha=datetime.datetime.now(),id_c=cuenta.objects.get(id_c=idcta))
    if (trans):
        efect=efectivo.objects.create(capital=monto,id_trans=transaccion.objects.get(id_t=trans.id_t))
    return redirect('/cuentas')

def abonar(request,idcta):
    monto=request.POST['num']
    trans=transaccion.objects.create(Abono=monto,id_c=cuenta.objects.get(id_c=idcta))
    return redirect('/cuentas')

def totalretiros(id):
    saldo=transaccion.objects.filter(id_c=id)
    totalRetiros=0
    totcompras=0
    if (saldo):
        for s in saldo:
            totalRetiros=s.retiro+totalRetiros        
    return totalRetiros


def totalabonos(id):
    saldo=transaccion.objects.filter(id_c=id)
    total=0
    if (saldo):
        for s in saldo:
            total=s.Abono+total
    return total

def operaciones(request):
    list=[]
    com=compra.objects.all()
    trans=transaccion.objects.all()
    for t in trans:
        acumRet=acumuladoretiros(t.fecha,t.id_c)#paso como parametro la fecha como maximo y la cuenta de la que quiero sacar el historial
        obj=compra.objects.filter(id_transaccion=t.id_t)  
        if (obj):
            print('existe')
            t.descrip=obj.get(id_transaccion=t.id_t).descripcion
            t.cantidad=obj.get(id_transaccion=t.id_t).cantidad
            t.precioU=obj.get(id_transaccion=t.id_t).precio_unitario
            t.subtotal=t.cantidad*t.precioU
            t.origen=t.id_c.banco
            t.capital=t.id_c.capital
            t.estadoCapital=t.id_c.capital - acumRet
            list.append(t)
        else:
            list.append(t)
            t.estadoCapital=t.id_c.capital - acumRet
            t.origen=t.id_c.banco
    return render(request,'Operaciones.html',{'transacciones':list})

def acumuladoretiros(id_f,id_cta):
    print(id_f)
    print(id_cta)
    retiros=transaccion.objects.filter(fecha__lte=id_f,id_c=id_cta)
    suma=0
    for ret in retiros:
        print(ret.retiro)
        suma=suma+ret.retiro
        print(suma)
    return suma
