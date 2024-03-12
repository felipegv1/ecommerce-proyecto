from rest_framework import serializers
from .models import Proveedor, Producto, Cliente


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProveedorProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    idProveedor = serializers.ReadOnlyField(source='proveedor.id')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion',
                  'precio', 'categoria', 'stock', 'idProveedor']


class ProveedorProductosSerializer(serializers.ModelSerializer):
    # 'producto_set' es el nombre de la relación inversa de Proveedor a Producto
    productos = ProductoSerializer(
        many=True, read_only=True, source='producto_set')

    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'telefono',
                  'email', 'direccion', 'productos']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
