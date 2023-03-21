from django.db import models

# Create your models here.


class Nota(models.Model):
    nombre_alumno = models.CharField(max_length=30),
    grado_alumno = models.CharField(max_length=15),
    nota_alumno = models.PositiveSmallIntegerField(null=True)

