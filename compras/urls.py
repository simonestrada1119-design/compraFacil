from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Proveedores
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/nuevo/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', views.proveedor_update, name='proveedor_update'),
    path('proveedores/eliminar/<int:pk>/', views.proveedor_delete, name='proveedor_delete'),
    
    # Compras
    path('compras/', views.compra_list, name='compra_list'),
    path('compras/nueva/', views.compra_create, name='compra_create'),
    path('compras/editar/<int:pk>/', views.compra_update, name='compra_update'),
    path('compras/eliminar/<int:pk>/', views.compra_delete, name='compra_delete'),
    path('proveedores/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
    path('compras/<int:pk>/', views.compra_detail, name='compra_detail'),
]