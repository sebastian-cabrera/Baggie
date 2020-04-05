from django.db import models

class Producto(models.Model):
    Tipo = models.CharField(max_length=15)
    Nombre = models.CharField(max_length=25)
    Procedencia = models.CharField(max_length=30)
    Variedad = models.CharField(max_length=15)
    Zafra = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre
