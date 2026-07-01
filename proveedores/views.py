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
    return render(request, 'proveedores/listar_proveedor.html', contexto)


@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get("nombre_empresa")
        ruc_proveedor = request.POST.get("ruc_proveedor")
        telefono_contacto = request.POST.get("telefono_contacto")
        direccion_matriz = request.POST.get("direccion_matriz")

        # Verificar si ya existe un proveedor con el mismo RUC
        if Proveedor.objects.filter(ruc_proveedor=ruc_proveedor).exists():
            messages.error(request, "El proveedor con este RUC ya existe")
            return render(request, "proveedores/crear_proveedor.html")

        # Crear proveedor
        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            ruc_proveedor=ruc_proveedor,
            telefono_contacto=telefono_contacto,
            direccion_matriz=direccion_matriz
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
        nombre_empresa = request.POST.get("nombre_empresa")
        ruc_proveedor = request.POST.get("ruc_proveedor")
        telefono_contacto = request.POST.get("telefono_contacto")
        direccion_matriz = request.POST.get("direccion_matriz")

        # Verificar RUC repetido
        if Proveedor.objects.filter(ruc_proveedor=ruc_proveedor).exclude(id=id).exists():
            messages.error(request, "El RUC del proveedor ya está registrado")
            return render(
                request,
                "proveedores/editar_proveedor.html",
                {"proveedor": proveedor}
            )

        # Actualizar datos
        proveedor.nombre_empresa = nombre_empresa
        proveedor.ruc_proveedor = ruc_proveedor
        proveedor.telefono_contacto = telefono_contacto
        proveedor.direccion_matriz = direccion_matriz

        proveedor.save()
        messages.success(request, "Proveedor actualizado con éxito")
        return redirect("listar_proveedores")

    contexto = {
        "proveedor": proveedor
    }

    return render(request, "proveedores/editar_proveedor.html", contexto)