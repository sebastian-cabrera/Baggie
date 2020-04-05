from django.db import models
class Usuario(models.Model):
    NIVEL_USUARIO = (
        ('1', 'Administrador'),
        ('2', 'Usuario'),
        ('3', 'Operador'),
    )
    creado_el = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    cedula = models.CharField(max_length=60)
    rol = models.CharField(max_length=1, choices=NIVEL_USUARIO)
    actividad_reciente = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
