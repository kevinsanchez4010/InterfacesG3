# views para el dashboard
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model

# usar get_user_model para soportar User customizado
User = get_user_model()
# Create your views here.

def dashboard(request):
    return render(request, 'private/dashboard.html')


def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios': usuarios

    }
    return render(request, 'private/listar_usuarios.html', contexto)

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)

        # si no existe el usuario
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, 'private/listar_usuarios.html')
        #si no existe el correo
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya existe')
            return render(request, 'private/listar_usuarios.html')
        
        #crear usuario
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Usuario creado exitosamente')
        return render(request, 'private/listar_usuarios.html')
    return render(request, 'private/crear_usuario.html')

def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado exitosamente')
    return redirect('listar_usuarios')
