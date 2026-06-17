from django.shortcuts import render

# Create your views here.

def listar_productos(request):
    return render(request, "productos/listar_productos.html")
