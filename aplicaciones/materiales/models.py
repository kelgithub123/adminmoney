from django.db import models
from ..CuentaBancaria.models import *
# Create your models here.
class compra(models.Model):
    id_compra=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25,default='No insertada')
    tipo=models.CharField(max_length=20)
    precio_unitario=models.FloatField(max_length=6)
    cantidad=models.FloatField(max_length=0)
    id_transaccion=models.ForeignKey(transaccion,on_delete=models.CASCADE,null=True)
    id_bill=models.ForeignKey(billetera,on_delete=models.CASCADE,null=True)