from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from proveedores.models import Proveedor


@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    contexto = {
        'proveedores': proveedores
    }
    return render(request, 'proveedores/listar_proveedores.html', contexto)


@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")
        direccion = request.POST.get("direccion")
        estado = request.POST.get("estado")

        # Verificar si ya existe un proveedor con el mismo nombre
        if Proveedor.objects.filter(nombre=nombre).exists():
            messages.error(request, "El proveedor ya existe")
            return render(request, "proveedores/crear_proveedor.html")

        # Crear proveedor
        Proveedor.objects.create(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            estado=estado
        )

        messages.success(request, "Proveedor creado con éxito")
        return redirect("listar_proveedores")

    return render(request, "proveedores/crear_proveedor.html")


@login_required
def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado")
    return redirect("listar_proveedores")


@login_required
def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)

    if request.method == "POST":
        nombre = request.POST.get("nombre_edit")
        telefono = request.POST.get("telefono_edit")
        correo = request.POST.get("correo_edit")
        direccion = request.POST.get("direccion_edit")
        estado = request.POST.get("estado_edit")

        # Verificar nombre repetido
        if Proveedor.objects.filter(nombre=nombre).exclude(id=id).exists():
            messages.error(request, "El nombre del proveedor ya está registrado")
            return render(
                request,
                "proveedores/editar_proveedor.html",
                {"proveedor": proveedor}
            )

        # Actualizar datos
        proveedor.nombre = nombre
        proveedor.telefono = telefono
        proveedor.correo = correo
        proveedor.direccion = direccion
        proveedor.estado = estado

        proveedor.save()
        messages.success(request, "Proveedor actualizado con éxito")
        return redirect("listar_proveedores")

    contexto = {
        "proveedor": proveedor
    }

    return render(request, "proveedores/editar_proveedor.html", contexto)