from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import Producto, Proveedor
from ..views.producto_views import *


class ProductoTest(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor test",
            telefono="123",
            email="proveedortest@ejemplo.com",
            direccion="direccion test"
        )

        self.producto1 = Producto.objects.create(
            nombre="Producto 1 Test",
            descripcion="Descripción 1",
            precio=100,
            categoria="Teclado",
            stock=10,
            proveedor=self.proveedor
        )
        self.producto2 = Producto.objects.create(
            nombre="Producto 2 Test",
            descripcion="Descripción 2",
            precio=200,
            categoria="Pantalla",
            stock=5,
            proveedor=self.proveedor
        )

    def testCrearProducto(self):
        producto = crearProducto(
            nombre="Producto 1",
            descripcion="Descripción",
            precio=10.0,
            categoria="Categoría",
            stock=10,
            proveedorId=self.proveedor.id
        )
        self.assertIsInstance(producto, Producto)
        self.assertEqual(producto.nombre, "Producto 1")

    def testProductoValidarCampos(self):
        with self.assertRaises(ValidationError):
            crearProducto(
                nombre="Producto 2",
                descripcion="Descripción",
                precio=20.0,
                categoria="",
                stock=20,
                proveedorId=self.proveedor.id
            )

    def test_proveedor_existente(self):
        with self.assertRaises(ValueError):
            Producto.objects.create(nombre="Producto 4", descripcion="Descripción",
                                    precio=20.0, categoria="Categoría", stock=20, proveedor=999)

    def testActualizarProducto(self):
        producto_actualizado = actualizarProducto(
            productoId=self.producto1.id,
            nombre="Nuevo Nombre",
            descripcion="Nueva descripción",
            precio=15.0,
            categoria="Nueva categoría",
            stock=25,
            proveedor_id=self.proveedor.id
        )
        self.assertEqual(producto_actualizado.nombre, "Nuevo Nombre")
        self.assertEqual(producto_actualizado.descripcion, "Nueva descripción")
        self.assertEqual(producto_actualizado.precio, 15.0)
        self.assertEqual(producto_actualizado.categoria, "Nueva categoría")
        self.assertEqual(producto_actualizado.stock, 25)
        self.assertEqual(producto_actualizado.proveedor, self.proveedor)

    def testValidacionNombreUnico(self):
        with self.assertRaises(ValidationError):
            actualizarProducto(
                productoId=self.producto1.id,
                nombre="Producto 2 Test",
                descripcion="Descripción",
                precio=15.0,
                categoria="Categoría",
                stock=25,
                proveedor_id=self.proveedor.id
            )

    # from rest_framework import status
    # from rest_framework.test import APITestCase
    # from ..serializers import ProductoSerializer
    # from django.urls import reverse

    # Test de integracion

    # def testObtenerProductosPorCategoria(self):
    #     # reverse genera una url con los argumentos dados
    #     url = reverse('obtenerProductosPorCategoria', args=["Teclado"])
    #     # simula una peticion GET a la api con la url
    #     response = self.client.get(url)
    #     teclados = Producto.objects.filter(categoria="Teclado")
    #     serializer = ProductoSerializer(teclados, many=True)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, serializer.data)

    # def testCrearProducto(self):
    #     url = reverse('crearProducto')
    #     nuevoProducto = {
    #         'nombre': 'Nuevo Producto test',
    #         'descripcion': 'Descripción 3',
    #         'precio': 150.00,
    #         'categoria': 'Teclado',
    #         'stock': 20,
    #         'proveedor': 1
    #     }
    #     response = self.client.post(url, nuevoProducto, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue(Producto.objects.filter(
    #         nombre='Nuevo Producto test').exists())

    # def testCrearProductoFallo(self):
    #     url = reverse('crearProducto')
    #     nuevoProducto = {
    #         # Sin nombre
    #         'descripcion': 'Descripción 3',
    #         'precio': 150.00,
    #         'categoria': 'Teclado',
    #         'stock': 20,
    #         'proveedor': 1
    #     }

    #     response = self.client.post(url, nuevoProducto, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
