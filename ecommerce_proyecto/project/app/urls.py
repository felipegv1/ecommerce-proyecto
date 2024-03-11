from django.urls import path
from .views.proveedor_views import proveedor_list, obtenerProveedorPorId, obtenerProveedorPorNombre
from .views.producto_views import productoList, obtenerProductoPorNombre, obtenerProductosPorCategoria, crearProducto

urlpatterns = [
    path('proveedores/', proveedor_list, name='proveedor-list'),
    path('proveedores/<int:id>/', obtenerProveedorPorId,
         name='obtenerProveedorPorId'),
    path('proveedores/<str:nombre>/', obtenerProveedorPorNombre,
         name='proveedor-por-nombre'),
    path('productos/', productoList,
         name='productoList'),
    path('productos/<str:nombre>/', obtenerProductoPorNombre,
         name='obtenerProductoPorNombre'),
    path('categoria/<str:categoria>/', obtenerProductosPorCategoria,
         name='obtenerProductosPorCategoria'),
    path('producto/crearProducto/', crearProducto, name='crearProducto'),

]
