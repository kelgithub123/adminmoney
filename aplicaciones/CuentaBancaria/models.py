from django.db import models
from django.utils import timezone,dates
import datetime

# Create your models here.
class cuenta(models.Model):
    id_c=models.AutoField(primary_key=True)
    banco=models.CharField (max_length=20)
    fecha=models.DateField(editable=True)
    tipo=models.CharField(max_length=10,default='corriente')
    interes=models.FloatField(max_length=6,default=0.00)  
    def __str__(self):
        texto = "{0}{1}"
        return texto.format(self.banco,self.id_c)


class billetera(models.Model):
    id_b=models.AutoField(primary_key=True,default=7)
    capital=models.FloatField(max_length=6)

class transaccion(models.Model):
    id_t=models.AutoField(primary_key=True)
    id_c=models.ForeignKey(cuenta,on_delete=models.CASCADE,null=True)
    id_bill=models.ForeignKey(billetera,on_delete=models.CASCADE,null=True)
    fechanow=datetime.date.today()
    format = fechanow.strftime('%Y'+'-'+'%m'+'-'+'%d')
    retiro=models.FloatField(max_length=6,default=0)
    Abono=models.FloatField(max_length=6,default=0)
    fecha=models.DateTimeField(default=datetime.datetime.now(),editable=True)

    def __str__(self):
        texto="{0}"
        return texto.format(self.id_t)