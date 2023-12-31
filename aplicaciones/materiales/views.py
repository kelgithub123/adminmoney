from django.shortcuts import render
from ..CuentaBancaria.models import *
# Create your views here.

def registrarcompra(request):
    cuentas=cuenta.objects.all()    
    return render(request,'cotizacion.html',{'cuenta':cuentas})