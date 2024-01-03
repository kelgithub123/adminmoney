from django.urls import path
from . import views

urlpatterns = [
    path('compra',views.compramenu),
    path('regispago',views.pagar),    
]