from django.test import TestCase
from django.urls import reverse
from ..models import Proveedor, Producto
from rest_framework.test import APITestCase
from rest_framework import status
from ..serializers import ProveedorProductosSerializer


class ProveedorTest(APITestCase):
    def setUp(self):
        proveedor = Proveedor.objects.create(
            nombre="Proveedor Uno",
            telefono="1234567890",
            email="email@ejemplo.com",
            direccion="direccion 1"
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

    def testProveedorProductos(self):
        url = reverse('proveedorPorNombre', args=["Proveedor Uno"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertIn("Proveedor Uno", response_data['nombre'])
        self.assertContains(response, "Proveedor Uno")
        self.assertContains(response, "Producto 2")

    def testProveedorProductosFallo(self):
        url = reverse('proveedorPorNombre', args=["ProveedorNoExistente"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
