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
    #cta=cuenta.objects.get(id_c=idcta)
    #cta.capital=cta.capital-float(monto)
    #cta.save()
    if (trans):
        efect=transaccion.objects.create(Abono=monto,id_bill=billetera.objects.get(id_b=7))
        #bill=billetera.objects.get(id_b=7)
        #bill.capital=bill.capital+float(monto)
        #bill.save()
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
    trans=transaccion.objects.all().order_by('id_c')
    for t in trans: 
            obj=compra.objects.filter(id_transaccion=t.id_t)  
            if (obj):
                print('existe')
                t.descrip=obj.get(id_transaccion=t.id_t).descripcion
                t.cantidad=obj.get(id_transaccion=t.id_t).cantidad
                t.precioU=obj.get(id_transaccion=t.id_t).precio_unitario
                t.subtotal=t.cantidad*t.precioU
                if(t.id_c):
                    acumRet=acumuladoretiros(t.id_t,t.id_c)#paso como parametro la fecha como maximo y la cuenta de la que quiero sacar el historial
                    acumAbo=acumuladoAbonos(t.id_t,t.id_c)
                    t.origen=t.id_c.banco
                    t.capital=t.id_c.capital
                    t.estadoCapital=t.id_c.capital - acumRet + acumAbo
                elif(t.id_bill):
                    acumRet=pagosbilletera(t.id_t,t.id_bill)
                    acumAbo=pagosbilletera(t.id_t,t.id_bill)
                    t.origen=t.id_bill.id_b
                    if(t.origen==7):
                        t.origen="CHEQUERA"
                    capital=AbonosBilletera()
                    t.capital=capital
                    t.chequera=t.capital- acumRet 
                list.append(t)
            elif(t.id_c):
                acumRet=acumuladoretiros(t.id_t,t.id_c)            
                t.estadoCap=t.id_c.capital - acumRet
                t.origen=t.id_c.banco
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