from django import forms
from django.utils import timezone
from .models import Proveedor, Compra


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["razon_social", "nit", "nombre_contacto", "telefono", "correo", "direccion"]
        widgets = {
            "razon_social": forms.TextInput(attrs={"maxlength": 150, "required": True}),
            "nit": forms.TextInput(attrs={"maxlength": 20, "required": True, "pattern": r"\d{6,15}(-\d)?", "title": "6 a 15 dígitos y guion opcional con dígito de verificación"}),
            "nombre_contacto": forms.TextInput(attrs={"maxlength": 120, "required": True}),
            "telefono": forms.TextInput(attrs={"maxlength": 20, "required": True, "pattern": r"[0-9+\-\s()]{7,20}"}),
            "correo": forms.EmailInput(attrs={"maxlength": 254, "required": True}),
            "direccion": forms.TextInput(attrs={"maxlength": 200, "required": True}),
        }

    def clean_nit(self):
        nit = self.cleaned_data["nit"].strip()
        qs = Proveedor.objects.filter(nit=nit)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un proveedor registrado con este NIT.")
        return nit

    def clean_razon_social(self):
        value = self.cleaned_data["razon_social"].strip()
        if not value:
            raise forms.ValidationError("La razón social es obligatoria.")
        return value


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["numero_compra", "proveedor", "fecha_compra", "descripcion", "valor_total", "estado"]
        widgets = {
            "numero_compra": forms.TextInput(attrs={"maxlength": 30, "required": True}),
            "proveedor": forms.Select(attrs={"required": True}),
            "fecha_compra": forms.DateInput(attrs={"type": "date", "required": True}),
            "descripcion": forms.Textarea(attrs={"rows": 3, "required": True}),
            "valor_total": forms.NumberInput(attrs={"min": "0.01", "step": "0.01", "required": True}),
            "estado": forms.Select(attrs={"required": True}),
        }

    def clean_numero_compra(self):
        numero = self.cleaned_data["numero_compra"].strip()
        qs = Compra.objects.filter(numero_compra=numero)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe una compra con este número.")
        return numero

    def clean_fecha_compra(self):
        fecha = self.cleaned_data["fecha_compra"]
        if fecha > timezone.localdate():
            raise forms.ValidationError("La fecha de compra no puede ser futura.")
        return fecha

    def clean_valor_total(self):
        valor = self.cleaned_data["valor_total"]
        if valor <= 0:
            raise forms.ValidationError("El valor total debe ser mayor que cero.")
        return valor

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"].strip()
        if not descripcion:
            raise forms.ValidationError("La descripción de la compra es obligatoria.")
        return descripcion
