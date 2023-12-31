from django.shortcuts import render,redirect
from .models import cuenta,transaccion
# Create your views here.
def menuRegcuenta(request):    
    return render(request,"registroCuenta.html",{"cuentas":"cuentas"})

def registrarcuenta(request):
    ban= request.POST['banco']
    cap=request.POST['capital']
    tip=request.POST['tipoDcuenta']
    inter=request.POST['interes']
    cuentas = cuenta.objects.create(banco=ban,capital=cap,tipo=tip,interes=inter)
    return redirect('/')

def listaDecuentas(request):
    cuentas=cuenta.objects.all()
    listcuentas=[]
    for ct in cuentas:
        totalretiros=totalretiros(ct.id_c)
        totalabonos=totalabonos(ct.id_c)
        ct.capital=ct.capital+totalabonos+totalretiros
        listcuentas.append(ct)
    ctafil=listcuentas

    return render(request,"ListaDcuentas.html",{"cuentas":ctafil})


def retirar(request,idcta,monto):
    ctadebitada=cuenta.objects.filter(id_c=idcta)
    trans=transaccion.objects.create(retiro=monto)
    return redirect('/cuentas')

def totalretiros(id):
    saldo=transaccion.objects.filter(id)
    for s in saldo:
        totalRetiros=s.retiro+totalRetiros
    return totalRetiros

def totalabonos(id):
    saldo=transaccion.objects.filter(id)
    for s in saldo:
        total=s.Abono+total
    return total