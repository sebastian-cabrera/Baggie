from django.db import models
class Usuario(models.Model):
    creado_el = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    cedula = models.CharField(max_length=60)
    rol = models.CharField(max_length=60)
    actividad_reciente = models.DateTimeField(auto_now_add=True)
