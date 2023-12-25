from django.db import models

# Create your models here.
class cuenta(models.Model):
    id_c=models.AutoField(primary_key=True)
    banco=models.CharField (max_length=20)
    capital=models.FloatField(max_length=6)
    tipo=models.CharField(max_length=10,default='corriente')
    interes=models.FloatField(max_length=6,default=0.00)  

    #def __str__(self):
        #texto = "{1} ({2})"

class operacion(models.Model):
    id=models.AutoField(primary_key=True)
    retiro=models.FloatField(max_length=6)
    Abono=models.FloatField(max_length=6)
    fecha=models.DateField