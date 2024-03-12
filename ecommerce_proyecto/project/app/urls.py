from django.urls import path
from .views.proveedor_views import proveedor_list, obtenerProveedorPorId, obtenerProveedorPorNombre
<<<<<<< HEAD
from .views.producto_views import productoList, obtenerProductoPorNombre, obtenerProductosPorCategoria, crearProducto
=======
from .views.producto_views import producto_list, obtenerProductoPorNombre
>>>>>>> 0f5425bda616039a9faf8a0645ec73267c12d3ac

urlpatterns = [
    path('proveedores/', proveedor_list, name='proveedor-list'),
    path('proveedores/<int:id>/', obtenerProveedorPorId,
         name='obtenerProveedorPorId'),
    path('proveedores/<str:nombre>/', obtenerProveedorPorNombre,
         name='proveedor-por-nombre'),
<<<<<<< HEAD
    path('productos/', productoList,
         name='productoList'),
    path('productos/<str:nombre>/', obtenerProductoPorNombre,
         name='obtenerProductoPorNombre'),
    path('categoria/<str:categoria>/', obtenerProductosPorCategoria,
         name='obtenerProductosPorCategoria'),
    path('producto/crearProducto/', crearProducto, name='crearProducto'),

=======
    path('productos/', producto_list, name='producto_list'),
    path('proveedores/<str:nombre>/', obtenerProductoPorNombre,
         name='proveedor-por-nombre'),
>>>>>>> 0f5425bda616039a9faf8a0645ec73267c12d3ac
]
