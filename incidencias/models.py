from django.db import models

from productos.models import Producto
from empaques.models import Empaque
from usuarios.models import Usuario

#
#   Modelo para definir Incidencias.
#

class Incidencia(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)
    Descripcion = models.CharField(max_length=25)
    Empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

#   Al consultar, nos devuelve el dato almacenado en el campo "Descripcion"

    def __str__(self):
        return self.Descripcion
