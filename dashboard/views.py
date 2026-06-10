from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def dashboard(request):
    return render(request, 'private/dashboard.html')


def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios': usuarios

    }
    return render(request, 'private/listar_usuarios.html', contexto)