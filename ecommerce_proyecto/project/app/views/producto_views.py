
from rest_framework.decorators import api_view
from ..models import Producto
from ..serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework import status


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
    return Response(serializer.data)


@api_view(['POST'])
def crearProducto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
