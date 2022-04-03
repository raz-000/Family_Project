from django.db import models

# Create your models here.
class Integrante_Familia(models.Model):
    nombre=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)
    edad=models.IntegerField()
    email=models.EmailField()
    descripcion=models.CharField(max_length=50)

