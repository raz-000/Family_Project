from django.db import models

# Create your models here.
class Integrante_Familia(models.Model):
    nombre=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)
    edad=models.IntegerField()
    email=models.EmailField()
    descripcion=models.CharField(max_length=50)
    nombre_mascota=models.CharField(max_length=40)

class Mascota(models.Model):
    nombre_mascota=models.CharField(max_length=40)
    edad_mascota=models.IntegerField()
    raza_mascota=models.CharField(max_length=40)

class Alimento(models.Model):
    nombre_mascota=models.CharField(max_length=40)
    marca_alimento=models.CharField(max_length=40)
    precio_dolares=models.IntegerField()


