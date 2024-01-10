from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from ..materiales.models import *
import datetime
# Create your views here.
def menuRegcuenta(request):    
    return render(request,"registroCuenta.html")

def eliminarTrans(request,id_tr):
    tr=transaccion.objects.get(id_t=id_tr)
    tr.delete()
    return redirect('/operaciones')

def registrarcuenta(request):
    ban= request.POST['banco']
    tip=request.POST['tipoDcuenta']
    inter=request.POST['interes']
    fec=request.POST['fecha']
    cuentas = cuenta.objects.create(banco=ban,tipo=tip,interes=inter,fecha=fec)
    return redirect('/')

def filtraEstadosCuenta():
    cuentas=cuenta.objects.all()
    listcuentas=[]
    for ct in cuentas:
        totalr=totalretiros(ct.id_c)
        totala=totalabonos(ct.id_c)
        ct.capital=totala-totalr
        ct.capini=totala
        ct.retiros=totalr
        ct.abonos=totala
        listcuentas.append(ct)
    return listcuentas

def listaDecuentas(request):
    ctafil=filtraEstadosCuenta
    return render(request,"ListaDcuentas.html",{"cuentas":ctafil})

def transferir(request,idcta):
    monto=request.POST['num']
    descr=request.POST['descrip']
    trans=transaccion.objects.create(retiro=monto,descripcion=descr,fecha=datetime.datetime.now(),id_c=cuenta.objects.get(id_c=idcta))
    return redirect('/cuentas')

def retirar(request,idcta):
    monto=request.POST['num']
    descr=request.POST['descrip']
    trans=transaccion.objects.create(retiro=monto,descripcion=descr,fecha=datetime.datetime.now(),id_c=cuenta.objects.get(id_c=idcta))
    if (trans):
        efect=transaccion.objects.create(Abono=monto,descripcion="ingreso efectivo",id_bill=billetera.objects.get(id_b=7))
    return redirect('/cuentas')

def abonar(request,idcta):
    monto=request.POST['num']
    descr=request.POST['descrip']
    trans=transaccion.objects.create(Abono=monto,descripcion=descr,id_c=cuenta.objects.get(id_c=idcta))
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

def compraEfectivo(request):
    list=[]
    com=compra.objects.all()
    capitalAnterior=AbonosBilletera()
    for c in com:
        if(c.id_transaccion.id_bill):    
            c.retiro=c.id_transaccion.retiro
            c.subtotal=c.cantidad*c.precio_unitario
            c.capital=capitalAnterior
            c.chequera= c.capital - c.subtotal
            c.fecha=c.id_transaccion.fecha    
            capitalAnterior=c.chequera
            list.append(c)               
    return render(request,'ComprasEfectivo.html',{'transacciones':list})

def operaciones(request):
    list=[]
    trans=transaccion.objects.all().order_by('id_c')
    capitalAntBanco=0
    capitalAnterior=0
    for t in trans: 
            if(t.id_c):
                acumRet=acumuladoretiros(t.id_t,t.id_c) #filtra y suma retiros hasta la fecha incluyendo el actual           
                acumAbo=acumuladoAbonos(t.id_t,t.id_c) #filtra y suma abonos hasta la fecha incluyendo el actual
                t.origen=t.id_c.banco
                t.capital=capitalAntBanco 
                t.estadoCapital= acumAbo - acumRet
                capitalAntBanco=t.estadoCapital
                list.append(t)           
    return render(request,'Operaciones.html',{'transacciones':list})

def acumuladoretiros(id_t,id_cta):
    print(id_t)
    print(id_cta)
    retiros=transaccion.objects.filter(id_c=id_cta,id_t__lte=id_t)
    suma=0
    for ret in retiros:
        print(ret.retiro)
        suma=suma+ret.retiro
    print("la suma es",suma)    
    return suma

def acumuladoAbonos(id_t,id_cta):
    print(id_t)
    print(id_cta)
    Abonos=transaccion.objects.filter(id_c=id_cta,id_t__lte=id_t)
    suma=0
    for Abon in Abonos:
        print(Abon.retiro)
        suma=suma+Abon.Abono
    print("la suma es",suma)    
    return suma

def pagosbilletera(id_t,idbill):
    retiros=transaccion.objects.filter(id_bill=idbill,id_t__lte=id_t)
    suma=0
    for ret in retiros:
        print(ret.retiro)
        suma=suma+ret.retiro
    print("la suma es",suma)    
    return suma

def abonosbilletera(id_t,idbill):
    abonos=transaccion.objects.filter(id_bill=idbill,id_t__lte=id_t)
    suma=0
    for abon in abonos:
        print(abon.Abono)
        suma=suma+abon.Abono
    print("la suma es",suma)    
    return suma

def AbonosBilletera():
    efectiv=transaccion.objects.filter(id_bill=billetera.objects.get(id_b=7))
    suma=0
    if(efectiv):
        for tr in efectiv:
            suma=tr.Abono+suma
    total=suma
    return total

def edicionTransaccion(request, id_tr):
    operacion = transaccion.objects.get(id_t=id_tr)
    return render(request, "editaroperacion.html", {"operacion": operacion})

def editarTrans(request,id_tr):
    #id_tr=request.GET['retiro']
    retiro = request.POST['retiro']
    abono = request.POST['abono']
    descrip=request.POST['descripcion']
    fecha = request.POST['fechaHora']
    trans = transaccion.objects.get(id_t=id_tr)
    trans.retiro = retiro
    trans.Abono = abono
    trans.descripcion = descrip
    trans.fecha = fecha
    trans.save()
    return redirect('/operaciones')
