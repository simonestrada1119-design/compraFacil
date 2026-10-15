import re
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator
from django.db import models
from django.utils import timezone


class Proveedor(models.Model):
    razon_social = models.CharField("Razón social", max_length=150)
    nit = models.CharField("NIT", max_length=20, unique=True)
    nombre_contacto = models.CharField("Nombre del contacto", max_length=120)
    telefono = models.CharField("Teléfono", max_length=20)
    correo = models.EmailField("Correo electrónico", max_length=254, validators=[EmailValidator()])
    direccion = models.CharField("Dirección", max_length=200)

    class Meta:
        ordering = ["razon_social"]
        constraints = [
            models.CheckConstraint(condition=~models.Q(razon_social=""), name="proveedor_razon_social_no_vacia"),
        ]

    def clean(self):
        super().clean()
        if not self.razon_social or not self.razon_social.strip():
            raise ValidationError({"razon_social": "La razón social es obligatoria."})
        if not self.nit or not self.nit.strip():
            raise ValidationError({"nit": "El NIT es obligatorio."})
        # Formato sencillo para este ejercicio: dígitos y guion opcional.
        if self.nit and not re.fullmatch(r"\d{6,15}(-\d)?", self.nit.strip()):
            raise ValidationError({"nit": "Usa entre 6 y 15 dígitos y, opcionalmente, guion y dígito de verificación."})
        if self.telefono and not re.fullmatch(r"[0-9+\-\s()]{7,20}", self.telefono.strip()):
            raise ValidationError({"telefono": "El teléfono contiene caracteres no permitidos."})
        for field in ("nombre_contacto", "direccion"):
            value = getattr(self, field)
            if not value or not value.strip():
                raise ValidationError({field: "Este campo es obligatorio."})

    def __str__(self):
        return f"{self.razon_social} ({self.nit})"


class Compra(models.Model):
    ESTADOS = [
        ("registrada", "Registrada"),
        ("recibida", "Recibida"),
        ("cancelada", "Cancelada"),
    ]
    numero_compra = models.CharField("Número de compra", max_length=30, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name="compras")
    fecha_compra = models.DateField("Fecha de compra", default=timezone.localdate)
    descripcion = models.TextField("Descripción")
    valor_total = models.DecimalField("Valor total", max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    estado = models.CharField("Estado", max_length=12, choices=ESTADOS, default="registrada")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="compras_registradas")

    class Meta:
        ordering = ["-fecha_compra", "-id"]
        constraints = [
            models.CheckConstraint(condition=models.Q(valor_total__gt=0), name="compra_valor_mayor_cero"),
        ]

    def clean(self):
        super().clean()
        if not self.numero_compra or not self.numero_compra.strip():
            raise ValidationError({"numero_compra": "El número de compra es obligatorio."})
        if not self.descripcion or not self.descripcion.strip():
            raise ValidationError({"descripcion": "La descripción es obligatoria."})
        if self.valor_total is not None and self.valor_total <= 0:
            raise ValidationError({"valor_total": "El valor total debe ser mayor que cero."})
        if self.estado not in dict(self.ESTADOS):
            raise ValidationError({"estado": "Selecciona un estado válido."})

    def __str__(self):
        return self.numero_compra
