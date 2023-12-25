from django.shortcuts import render,redirect
from .models import cuenta
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
    return render(request,"ListaDcuentas.html",{"cuentas":cuentas})
