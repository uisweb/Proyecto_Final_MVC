from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    tipodocumento = models.CharField(max_length = 5)
    documento = models.CharField(max_length = 40)
    lu_residencia = models.CharField(max_length = 50)
    fecha_na = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 80)
    telefono = models.BigIntegerField()
    usuario = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre
