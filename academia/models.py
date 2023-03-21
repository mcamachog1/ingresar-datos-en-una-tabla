from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
import datetime
# Create your models here.


# class Nota(models.Model):
#     nombre_alumno = models.CharField(max_length=30, null=True),
#     apellido_alumno = models.CharField(max_length=30, null=True),
#     grado_alumno = models.CharField(max_length=15, null=True),
#     puntos_alumno = models.PositiveSmallIntegerField(null=True)

class Evaluacion(models.Model):
	nombre = models.CharField(max_length=30, blank=False)
	apellido = models.CharField(max_length=30)
	email = models.EmailField(max_length=254, null=True)
	fecha_nacimiento = models.DateTimeField(null=True)
	nota = models.PositiveSmallIntegerField(null=True)

