from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuRegcuenta,name='inicio'),
    path('RegCuentas',views.registrarcuenta),
    path('cuentas',views.listaDecuentas),
    path('retiro/<idcta>',views.retirar),
    path('abono/<idcta>',views.abonar),
    path('transferir/<idcta>',views.transferir),
    path('eliminarTrans/<id_tr>',views.eliminarTrans),
    path('operaciones',views.operaciones)    
]