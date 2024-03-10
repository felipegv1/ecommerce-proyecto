from models.FacturaProducto import FacturaProducto


def ventas_producto_fecha(producto_id, fecha):
    venta = FacturaProducto.objects.filter(
        producto_id=producto_id,
        factura__fecha__date=fecha
    )
    if venta.exists():
        return True, venta
    else:
        return False, "No se registraron ventas para este producto en la fecha especificada."
