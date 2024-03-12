from django.test import TestCase
from django.urls import reverse
from ..models import Producto
from ..models import Proveedor
from rest_framework import status
from rest_framework.test import APITestCase
from ..serializers import ProductoSerializer


class ProductoTest(APITestCase):
    def setUp(self):
        proveedor = Proveedor.objects.create(
            nombre="Proveedor test",
            telefono="123",
            email="proveedortest@ejemplo.com",
            direccion="direccion test"
        )

        Producto.objects.create(
            nombre="Producto 1 Test",
            descripcion="Descripción 1",
            precio=100,
            categoria="Teclado",
            stock=10,
            proveedor=proveedor
        )
        Producto.objects.create(
            nombre="Producto 2 Test",
            descripcion="Descripción 2",
            precio=200,
            categoria="Pantalla",
            stock=5,
            proveedor=proveedor
        )

    def testObtenerProductosPorCategoria(self):
        # reverse genera una url con los argumentos dados
        url = reverse('obtenerProductosPorCategoria', args=["Teclado"])
        # simula una peticion GET a la api con la url
        response = self.client.get(url)
        productos_esperados = Producto.objects.filter(categoria="Teclado")
        serializer = ProductoSerializer(productos_esperados, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def testObtenerProductosPorCategoriaNoEncontrado(self):
        # reverse genera una url con los argumentos dados
        url = reverse('obtenerProductosPorCategoria', args=["Pantallas"])
        # simula una peticion GET a la api con la url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def testCrearProducto(self):
        pass
