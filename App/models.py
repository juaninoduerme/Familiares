from django.db import models

# Create your models here.
class Familiar(models.Model):
    idFamiliar = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField(max_length=30)
    dni = models.IntegerField()
    parentezco = models.CharField(max_length=30)