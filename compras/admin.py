from django.contrib import admin
from .models import Proveedor, Compra

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("razon_social", "nit", "nombre_contacto", "telefono", "correo")
    search_fields = ("razon_social", "nit")

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("numero_compra", "proveedor", "fecha_compra", "valor_total", "estado", "usuario")
    list_filter = ("estado", "fecha_compra")
    search_fields = ("numero_compra", "proveedor__razon_social")
