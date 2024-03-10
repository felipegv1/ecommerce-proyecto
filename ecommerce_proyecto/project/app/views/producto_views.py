from models.Producto import Producto


def buscar_productos_por_categoria(nombre_categoria):
    productos = Producto.objects.filter(categoria=nombre_categoria)
    if productos.exists():
        return True, productos
    else:
        return False, "No se encontraron productos para la categoría proporcionada."


def eliminar_producto(producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        producto.delete()
        return True, "Producto eliminado correctamente."
    except Producto.DoesNotExist:
        return False, "Producto no encontrado."


def crear_producto(nombre, descripcion, precio, categoria, stock, proveedor):
    producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio,
                        categoria=categoria, stock=stock, proveedor=proveedor)
    producto.save()
    return producto


def listar_productos_por_categoria(categoria):
    return Producto.objects.filter(categoria=categoria)


def incrementar_stock_producto(producto_id, cantidad):
    producto = Producto.objects.get(pk=producto_id)
    producto.stock += cantidad
    producto.save()
    return producto
