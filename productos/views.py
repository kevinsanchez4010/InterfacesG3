from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import redirect, render
from productos.models import Producto
# Create your views here.

@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'productos/listar_productos.html', contexto)

@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        estado = request.POST.get("estado")

        # Si ya existe un producto con el mismo nombre
        if Producto.objects.filter(nombre=nombre).exists():
            messages.error(request, "El producto ya existe")
            return render(request, "productos/crear_producto.html")

        # Crear producto
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            estado=estado
        )

        messages.success(request, "Producto creado con éxito")
        return redirect("listar_productos")
        
    return render(request, "productos/crear_producto.html")

@login_required
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "Producto eliminado")
    return redirect("listar_productos")

@login_required
def editar_producto(request, id): # Método editar
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        nombre = request.POST.get("nombre_edit")
        precio = request.POST.get("precio_edit")
        stock = request.POST.get("stock_edit")
        estado = request.POST.get("estado_edit")

        # Verificar si existe el nombre excluyendo el producto actual
        if Producto.objects.filter(nombre=nombre).exclude(id=id).exists():
            messages.error(request, "El nombre del producto ya está registrado")
            return render(request, "productos/editar_producto.html", {"producto": producto})
        
        # Actualizar datos
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.estado = estado
        
        producto.save()
        messages.success(request, "El producto se actualizó con éxito")
        return redirect("listar_productos")
        
    contexto = {
        "producto": producto
    }
    return render(request, "productos/editar_producto.html", contexto)