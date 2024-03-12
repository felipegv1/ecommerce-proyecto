from django.urls import path, include
from .views.proveedor_views import proveedorList, obtenerProveedorPorId, obtenerProveedorPorNombre
from .views.producto_views import productoList, obtenerProductoPorNombre, obtenerProductosPorCategoria, crearProducto

urlpatterns = [
    path('proveedores/', include([
        path('', proveedorList, name='proveedorList'),
        path('<int:id>/', obtenerProveedorPorId,
             name='obtenerProveedorPorId'),
        path('<str:nombre>/', obtenerProveedorPorNombre,
             name='proveedorPorNombre'),
    ])),
    path('productos/', include([
        path('', productoList, name='productoList'),
        path('crearProducto/', crearProducto, name='crearProducto'),
        path('<str:nombre>/', obtenerProductoPorNombre,
             name='obtenerProductoPorNombre'),
        path('categoria/<str:categoria>/', obtenerProductosPorCategoria,
             name='obtenerProductosPorCategoria'),
    ])),
]
