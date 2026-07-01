from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import OrdenSalida


def listar_ordenes_salida(request):
    ordenes_salida = OrdenSalida.objects.all()
    return render(request, 'ordenes_salida/listar_ordenes_salida.html', {'ordenes_salida': ordenes_salida})


def crear_orden_salida(request):
    if request.method == 'POST':
        proveedor = request.POST.get('proveedor')
        producto = request.POST.get('producto')
        categoria = request.POST.get('categoria')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('precio_unitario')
        fecha_salida = request.POST.get('fecha_salida')
        observaciones = request.POST.get('observaciones')

        OrdenSalida.objects.create(
            proveedor=proveedor,
            producto=producto,
            categoria=categoria,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            fecha_salida=fecha_salida,
            usuario=request.user,
            observaciones=observaciones,
        )
        messages.success(request, 'Orden de salida registrada exitosamente')
        return redirect('listar_ordenes_salida')

    return render(request, 'ordenes_salida/crear_orden_salida.html')


def eliminar_orden_salida(request, id):
    orden = get_object_or_404(OrdenSalida, id=id)
    orden.delete()
    messages.success(request, 'Orden de salida eliminada exitosamente')
    return redirect('listar_ordenes_salida')


def editar_orden_salida(request, id):
    orden = get_object_or_404(OrdenSalida, id=id)
    if request.method == 'POST':
        orden.proveedor = request.POST.get('proveedor')
        orden.producto = request.POST.get('producto')
        orden.categoria = request.POST.get('categoria')
        orden.cantidad = request.POST.get('cantidad')
        orden.precio_unitario = request.POST.get('precio_unitario')
        orden.fecha_salida = request.POST.get('fecha_salida')
        orden.observaciones = request.POST.get('observaciones')
        orden.usuario = request.user
        orden.save()
        messages.success(request, 'Orden de salida actualizada exitosamente')
        return redirect('listar_ordenes_salida')

    return render(request, 'ordenes_salida/editar_orden_salida.html', {'orden': orden})
