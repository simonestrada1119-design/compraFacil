from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProveedorForm, CompraForm
from .models import Proveedor, Compra


@login_required
def inicio(request):
    return render(request, "compras/inicio.html", {
        "total_proveedores": Proveedor.objects.count(),
        "total_compras": Compra.objects.count(),
        "compras_recientes": Compra.objects.select_related("proveedor", "usuario")[:5],
    })


@login_required
def proveedores_lista(request):
    q = request.GET.get("q", "").strip()
    proveedores = Proveedor.objects.all()
    if q:
        proveedores = proveedores.filter(Q(razon_social__icontains=q) | Q(nit__icontains=q))
    return render(request, "compras/proveedores_lista.html", {"proveedores": proveedores, "q": q})


@login_required
def proveedor_crear(request):
    form = ProveedorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proveedor registrado correctamente.")
        return redirect("proveedores_lista")
    return render(request, "compras/formulario.html", {"form": form, "titulo": "Registrar proveedor", "volver": "proveedores_lista"})


@login_required
def proveedor_editar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proveedor actualizado correctamente.")
        return redirect("proveedores_lista")
    return render(request, "compras/formulario.html", {"form": form, "titulo": "Editar proveedor", "volver": "proveedores_lista"})


@login_required
def proveedor_detalle(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "compras/proveedor_detalle.html", {"proveedor": proveedor})


@login_required
def proveedor_eliminar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        if proveedor.compras.exists():
            messages.error(request, "No puedes eliminar un proveedor que tiene compras asociadas.")
        else:
            proveedor.delete()
            messages.success(request, "Proveedor eliminado correctamente.")
        return redirect("proveedores_lista")
    return render(request, "compras/confirmar_eliminar.html", {"objeto": proveedor, "titulo": "Eliminar proveedor", "volver": "proveedores_lista"})


@login_required
def compras_lista(request):
    estado = request.GET.get("estado", "")
    proveedor_id = request.GET.get("proveedor", "")
    compras = Compra.objects.select_related("proveedor", "usuario").all()
    if estado in dict(Compra.ESTADOS):
        compras = compras.filter(estado=estado)
    else:
        estado = ""
    if proveedor_id.isdigit():
        compras = compras.filter(proveedor_id=int(proveedor_id))
    else:
        proveedor_id = ""
    return render(request, "compras/compras_lista.html", {
        "compras": compras, "estados": Compra.ESTADOS, "estado_seleccionado": estado,
        "proveedores": Proveedor.objects.all(), "proveedor_seleccionado": proveedor_id,
    })


@login_required
def compra_crear(request):
    form = CompraForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        compra = form.save(commit=False)
        compra.usuario = request.user
        compra.save()
        messages.success(request, "Compra registrada correctamente.")
        return redirect("compras_lista")
    return render(request, "compras/formulario.html", {"form": form, "titulo": "Registrar compra", "volver": "compras_lista"})


@login_required
def compra_editar(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    form = CompraForm(request.POST or None, instance=compra)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Compra actualizada correctamente.")
        return redirect("compras_lista")
    return render(request, "compras/formulario.html", {"form": form, "titulo": "Editar compra", "volver": "compras_lista"})


@login_required
def compra_detalle(request, pk):
    compra = get_object_or_404(Compra.objects.select_related("proveedor", "usuario"), pk=pk)
    return render(request, "compras/compra_detalle.html", {"compra": compra})


@login_required
def compra_eliminar(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == "POST":
        compra.delete()
        messages.success(request, "Compra eliminada correctamente.")
        return redirect("compras_lista")
    return render(request, "compras/confirmar_eliminar.html", {"objeto": compra, "titulo": "Eliminar compra", "volver": "compras_lista"})
