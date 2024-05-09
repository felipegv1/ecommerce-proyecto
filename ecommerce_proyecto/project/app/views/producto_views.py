
from rest_framework.decorators import api_view
from ..models import Producto, Proveedor
from ..serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework import status


def crearProducto(nombre, descripcion, precio, categoria, stock, proveedorId):
    proveedor = Proveedor.objects.get(id=proveedorId)

    producto = Producto(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        categoria=categoria,
        stock=stock,
        proveedor=proveedor
    )
    producto.full_clean()
    producto.save()

    return producto


def actualizarProducto(productoId, nombre, descripcion, precio, categoria, stock, proveedor_id):
    producto = Producto.objects.get(pk=productoId)

    proveedor = Proveedor.objects.get(id=proveedor_id)

    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.categoria = categoria
    producto.stock = stock
    producto.proveedor = proveedor

    producto.full_clean()
    producto.save()

    return producto


@api_view(['GET'])
def productoList(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def obtenerProductoPorNombre(request, nombre):
    try:
        producto = Producto.objects.get(nombre=nombre)
    except Producto.DoesNotExist:
        return Response({"mensaje": "producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)


@api_view(['GET'])
def obtenerProductosPorCategoria(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def crearProducto(request):
#     serializer = ProductoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
