from django.db import models

# Create your models here.

class Clases(models.Model):
    nombre = models.CharField(max_length=164)
    dia = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

class Alumnos(models.Model):
    apellido = models.CharField(max_length=256)
    nombre =  models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nac = models.DateField()


class Profesores(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nac = models.DateField()
