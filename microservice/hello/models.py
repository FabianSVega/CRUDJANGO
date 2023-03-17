from django.db import models

# Create your models here.
class Task(models.Model):
    codigo =    models.IntegerField(10)
    nif    =    models.CharField(max_length=100)
    nombre =    models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.IntegerField(10)
    
    def __str__(self):
        return self