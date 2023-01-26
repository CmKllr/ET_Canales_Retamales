from django.db import models

# Create your models here.


class Viaje(models.Model):
    codigo=models.CharField(max_length=8, primary_key=True, verbose_name='Codigo')
    destino=models.CharField(max_length=40, verbose_name='Destino')
    cantidadPasajero=models.CharField(max_length=5000, verbose_name='CantidadPasajero')
    distanciaRecorrer=models.CharField(max_length=1000000000, verbose_name='DistanciaRecorrer')

    def __str__(self):
        return self.codigo



class Cliente(models.Model):
    rut=models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=40, verbose_name='Nombre')
    edad=models.CharField(max_length=250, verbose_name='Edad')
    correo=models.CharField(max_length=40, verbose_name='Correo')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    
    def str(self):
        return self.rut
