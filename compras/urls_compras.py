from django.urls import path
from . import views

urlpatterns = [
    path("", views.compras_lista, name="compras_lista"),
    path("nueva/", views.compra_crear, name="compra_crear"),
    path("<int:pk>/", views.compra_detalle, name="compra_detalle"),
    path("<int:pk>/editar/", views.compra_editar, name="compra_editar"),
    path("<int:pk>/eliminar/", views.compra_eliminar, name="compra_eliminar"),
]
