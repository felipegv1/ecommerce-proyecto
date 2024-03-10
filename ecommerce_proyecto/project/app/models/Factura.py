from django.db import models
from .Cliente import Cliente


class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, null=True)
