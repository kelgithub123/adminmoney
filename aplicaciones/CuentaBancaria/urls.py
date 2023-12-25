from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuRegcuenta,name='inicio'),
    path('RegCuentas',views.registrarcuenta),
    path('cuentas',views.listaDecuentas)    
]