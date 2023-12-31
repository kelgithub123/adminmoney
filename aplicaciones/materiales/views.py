from django.shortcuts import render
from ..CuentaBancaria.models import *
from ..CuentaBancaria.views import *
# Create your views here.

def registrarcompra(request):
    cuentas=filtraEstadosCuenta()
    return render(request,'cotizacion.html',{'cuenta':cuentas})