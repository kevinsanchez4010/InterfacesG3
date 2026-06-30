from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import OrdenEntrada


def listar_ordenes_entrada(request):
    ordenes_entrada = OrdenEntrada.objects.all()
    return render(request, 'ordenes_entrada/listar_ordenes_entrada.html', {'ordenes_entrada': ordenes_entrada})


def crear_orden_entrada(request):
    if request.method == 'POST':
        proveedor = request.POST.get('proveedor')
        producto = request.POST.get('producto')
        categoria = request.POST.get('categoria')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('precio_unitario')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        observaciones = request.POST.get('observaciones')

        OrdenEntrada.objects.create(
            proveedor=proveedor,
            producto=producto,
            categoria=categoria,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            fecha_ingreso=fecha_ingreso,
            usuario=request.user,
            observaciones=observaciones,
        )
        messages.success(request, 'Orden de entrada registrada exitosamente')
        return redirect('listar_ordenes_entrada')

    return render(request, 'ordenes_entrada/crear_orden_entrada.html')


def eliminar_orden_entrada(request, id):
    orden = get_object_or_404(OrdenEntrada, id=id)
    orden.delete()
    messages.success(request, 'Orden de entrada eliminada exitosamente')
    return redirect('listar_ordenes_entrada')


def editar_orden_entrada(request, id):
    orden = get_object_or_404(OrdenEntrada, id=id)
    if request.method == 'POST':
        orden.proveedor = request.POST.get('proveedor')
        orden.producto = request.POST.get('producto')
        orden.categoria = request.POST.get('categoria')
        orden.cantidad = request.POST.get('cantidad')
        orden.precio_unitario = request.POST.get('precio_unitario')
        orden.fecha_ingreso = request.POST.get('fecha_ingreso')
        orden.observaciones = request.POST.get('observaciones')
        orden.usuario = request.user
        orden.save()
        messages.success(request, 'Orden de entrada actualizada exitosamente')
        return redirect('listar_ordenes_entrada')

    return render(request, 'ordenes_entrada/editar_orden_entrada.html', {'orden': orden})
