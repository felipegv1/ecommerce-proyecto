from django.db import models
from .Proveedor import Proveedor


class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(default='')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    categoria = models.TextField(default='')
    stock = models.IntegerField(default='')
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True)

    # imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
