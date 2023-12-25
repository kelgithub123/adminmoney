from django.db import models

# Create your models here.
class materiales(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=35)
    cantidad=models.IntegerField
    unidad=models.CharField(max_length=3)
    precio=models.FloatField(max_length=6)
    preciounit=models.FloatField(max_length=6)
    
    def __str__(self):
        texto="{1} {2} {5}" 
        return texto.format(self.nombre,self.cantidad,self.preciounit)
        