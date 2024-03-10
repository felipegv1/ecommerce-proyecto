from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(default='', unique=True)
    direccion = models.TextField(default='')
    telefono = models.CharField(default='', max_length=10)
