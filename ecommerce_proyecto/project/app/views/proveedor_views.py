
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Proveedor
from ..serializers import ProveedorSerializer


# Indica que esta vista acepta los métodos GET y POST.
@api_view(['GET', 'POST'])
def proveedor_list(request):
    if request.method == 'GET':
        # Si la solicitud es GET, obtenemos todos los proveedores y devolvemos su información.
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Si la solicitud es POST, creamos un nuevo proveedor con los datos proporcionados.
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProveedorList(generics.ListAPIView):
#     queryset = Proveedor.objects.all()
#     serializer_class = ProveedorSerializer


# def actualizar_direccion_proveedor(proveedor_id, nueva_direccion):
#     try:
#         proveedor = Proveedor.objects.get(pk=proveedor_id)
#         proveedor.direccion = nueva_direccion
#         proveedor.save()
#         return True, "Dirección del proveedor actualizada correctamente."
#     except Proveedor.DoesNotExist:
#         return False, "Proveedor no encontrado."
