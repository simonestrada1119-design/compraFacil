from django.urls import path
from . import views

urlpatterns = [
    path("", views.proveedores_lista, name="proveedores_lista"),
    path("nuevo/", views.proveedor_crear, name="proveedor_crear"),
    path("<int:pk>/", views.proveedor_detalle, name="proveedor_detalle"),
    path("<int:pk>/editar/", views.proveedor_editar, name="proveedor_editar"),
    path("<int:pk>/eliminar/", views.proveedor_eliminar, name="proveedor_eliminar"),
]
