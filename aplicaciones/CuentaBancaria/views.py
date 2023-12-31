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
    totalRetiros=0
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