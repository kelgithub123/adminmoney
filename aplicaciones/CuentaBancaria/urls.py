from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuRegcuenta,name='inicio'),
    path('RegCuentas',views.registrarcuenta),
    path('cuentas',views.listaDecuentas),
<<<<<<< HEAD
    path('retiro/<idcta>/<monto>',views.retirar)    
=======
    path('retiro/<idcta>',views.retirar),
    path('abono/<idcta>',views.abonar)    
>>>>>>> tmp
]