from django.db import models

class Empaque(models.Model):
    Tipo = models.CharField(max_length=15)
    Proveedor = models.CharField(max_length=25)
    Modelo = models.CharField(max_length=30)
    Dimensiones = models.CharField(max_length=15)
    Peso_Max = models.IntegerField(default=0)
    Cantidad_Usos = models.IntegerField(default=0)

    def __str__(self):
        return self.Tipo
