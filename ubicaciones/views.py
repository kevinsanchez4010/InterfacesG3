from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ubicaciones.models import Ubicacion as Ubicaciones

# Create your views here.

# Mostrar
@login_required
def listar_ubicaciones(request):
    ubicaciones = Ubicaciones.objects.all()
    contexto = {
        'ubicaciones': ubicaciones
    }
    return render(request, 'ubicaciones/listar_ubicaciones.html', contexto)

# Crear
@login_required
def crear_ubicacion(request):
    if request.method == 'POST':
        nombre_area = request.POST.get("nombre_area")
        capacidad_maxima = request.POST.get("capacidad_maxima")
        seccion_fila = request.POST.get("seccion_fila")
        estado_espacio = request.POST.get("estado_espacio")

        # Validar si ya existe una ubicación con ese nombre de área en esa sección específica
        if Ubicaciones.objects.filter(nombre_area=nombre_area, seccion_fila=seccion_fila).exists():
            messages.error(request, "Esta ubicación (Área y Sección/Fila) ya se encuentra registrada")
            return render(request, "ubicaciones/crear_ubicacion.html")

        # Crear ubicación
        Ubicaciones.objects.create(
            nombre_area=nombre_area,
            capacidad_maxima=capacidad_maxima,
            seccion_fila=seccion_fila,
            estado_espacio=estado_espacio
        )

        messages.success(request, "Ubicación creada con éxito")
        return redirect("listar_ubicaciones")
        
    return render(request, "ubicaciones/crear_ubicacion.html")

# Eliminar
@login_required
def eliminar_ubicacion(request, id):
    try:
        ubicacion = Ubicaciones.objects.get(id=id)
        ubicacion.delete()
        messages.success(request, "Ubicación eliminada con éxito")
    except Exception:
        # Por si intentan borrar una ubicación que tiene productos (on_delete=models.PROTECT)
        messages.error(request, "No se puede eliminar esta ubicación porque contiene productos almacenados.")
        
    return redirect("listar_ubicaciones")

# Editar
@login_required
def editar_ubicacion(request, id):
    ubicacion = Ubicaciones.objects.get(id=id)
    
    if request.method == 'POST':
        nombre_area = request.POST.get("nombre_area")
        capacidad_maxima = request.POST.get("capacidad_maxima")
        seccion_fila = request.POST.get("seccion_fila")
        estado_espacio = request.POST.get("estado_espacio")

        # Validar si ya existe otra ubicación idéntica pero con diferente ID
        if Ubicaciones.objects.filter(nombre_area=nombre_area, seccion_fila=seccion_fila).exclude(id=id).exists():
            messages.error(request, "Esa combinación de Área y Sección ya pertenece a otra ubicación")
            return render(request, "ubicaciones/editar_ubicacion.html", {'ubicacion': ubicacion})

        # Actualizar ubicación
        ubicacion.nombre_area = nombre_area
        ubicacion.capacidad_maxima = capacidad_maxima
        ubicacion.seccion_fila = seccion_fila
        ubicacion.estado_espacio = estado_espacio
        ubicacion.save()

        messages.success(request, "Ubicación actualizada con éxito")
        return redirect("listar_ubicaciones")

    return render(request, "ubicaciones/editar_ubicacion.html", {'ubicacion': ubicacion})