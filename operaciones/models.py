from django.db import models
from empaques.models import Empaque
from productos.models import Producto
from django.contrib.auth.models import User

class Movimiento(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)
    Descripcion = models.CharField(max_length=25)
    ID_Empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE)
    ID_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ID_Usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion
