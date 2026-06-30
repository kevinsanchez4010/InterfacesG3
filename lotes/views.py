from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect
from proveedores.models import Lotes
# Create your views here.

#Mostrar
@login_required
def listar_lotes(request):
    lotes = Lotes.objects.all()
    contexto = {
        'lotes': lotes
    }
    return render(request, 'lotes/listar_lotes.html', contexto)

#Crear
@login_required
def crear_lote(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        cantidad = request.POST.get("cantidad")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")
        estado = request.POST.get("estado")

        #Si ya existe un lote
        if Lotes.objects.filter(nombre=nombre).exists():
            messages.error(request, "El lote ya existe")
            return render(request, "lotes/crear_lote.html")

        #Crear lote
        Lotes.objects.create(
            nombre=nombre,
            cantidad=cantidad,
            fecha_vencimiento=fecha_vencimiento,
            estado=estado
        )

        messages.success(request, "Lote creado con éxito")
        return redirect("listar_lotes")
        
    return render(request, "lotes/crear_lote.html")

#Eliminar
@login_required
def eliminar_lote(request, id):
    lote = Lotes.objects.get(id=id)
    lote.delete()
    messages.success(request, "Lote eliminado con éxito")
    return redirect("listar_lotes")

#Editar
@login_required
def editar_lote(request, id):
    lote = Lotes.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        cantidad = request.POST.get("cantidad")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")
        estado = request.POST.get("estado")

        # Si ya existe un lote con el mismo nombre (y es diferente del actual)
        if Lotes.objects.filter(nombre=nombre).exclude(id=id).exists():
            messages.error(request, "El lote ya existe")
            return render(request, "lotes/editar_lote.html", {'lote': lote})

        # Actualizar lote
        lote.nombre = nombre
        lote.cantidad = cantidad
        lote.fecha_vencimiento = fecha_vencimiento
        lote.estado = estado
        lote.save()

        messages.success(request, "Lote actualizado con éxito")
        return redirect("listar_lotes")

    return render(request, "lotes/editar_lote.html", {'lote': lote})