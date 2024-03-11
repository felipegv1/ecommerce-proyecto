from django.urls import path
from .views.proveedor_views import proveedor_list, obtenerProveedorPorId, obtenerProveedorPorNombre
from .views.producto_views import producto_list, obtenerProductoPorNombre

urlpatterns = [
    path('proveedores/', proveedor_list, name='proveedor-list'),
    path('proveedores/<int:id>/', obtenerProveedorPorId,
         name='obtenerProveedorPorId'),
    path('proveedores/<str:nombre>/', obtenerProveedorPorNombre,
         name='proveedor-por-nombre'),
    path('productos/', producto_list, name='producto_list'),
    path('proveedores/<str:nombre>/', obtenerProductoPorNombre,
         name='proveedor-por-nombre'),
]
