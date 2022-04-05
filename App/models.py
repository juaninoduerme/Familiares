from django.db import models

# Create your models here.
class Familiar(models.Model):
    idFamiliar = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaDeNacimiento = models.DateField()
    dni = models.IntegerField()
    parentezco = models.CharField(max_length=30)