
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Proveedor
from ..serializers import ProveedorSerializer, ProveedorProductosSerializer


@api_view(['GET'])
def obtenerProveedorPorNombre(request, nombre):
    try:
        proveedor = Proveedor.objects.get(nombre=nombre)
    except Proveedor.DoesNotExist:
        return Response({"mensaje": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProveedorProductosSerializer(proveedor)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def obtenerProveedorPorId(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({"mensaje": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def proveedorList(request):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
