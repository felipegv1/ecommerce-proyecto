from django.urls import path
from .views.proveedor_views import proveedor_list

urlpatterns = [
    path('proveedores/', proveedor_list, name='proveedor-list'),
]
