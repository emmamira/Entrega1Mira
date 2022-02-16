from django.db import models

# Create your models here.
class Liga(models.Model):
    nombre=models.CharField(max_length=30)
    cantidadEquipos=models.IntegerField()

class Equipo(models.Model):
    nombre=models.CharField(max_length=30)
    ciudad=models.CharField(max_length=30)
    añoFundación=models.IntegerField()

class Partido(models.Model):
    fecha=models.DateField()
    cancha=models.CharField(max_length=30)
    local=models.CharField(max_length=30)
    visitante=models.CharField(max_length=30)
    jugado=models.BooleanField()

class Goleador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    equipo=models.CharField(max_length=30)
    goles=models.IntegerField()