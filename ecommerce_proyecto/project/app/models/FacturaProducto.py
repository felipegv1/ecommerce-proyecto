from django.db import models
from .Factura import Factura
from .Producto import Producto


class FacturaProducto(models.Model):
    factura = models.ForeignKey(
        Factura, on_delete=models.CASCADE, related_name='factura_productos')
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='factura_productos')
    cantidad = models.IntegerField()
