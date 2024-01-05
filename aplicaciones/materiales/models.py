from django.db import models
from ..CuentaBancaria.models import *
# Create your models here.
class compra(models.Model):
    id_compra=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25,default='No insertada')
    tipo=models.CharField(max_length=20)
    precio_unitario=models.FloatField(max_length=6)
    cantidad=models.IntegerField(max_length=6,default=0)
    id_transaccion=models.ForeignKey(transaccion,on_delete=models.CASCADE,default=0)