from django.contrib import messages

from django.shortcuts import redirect, render
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

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        #si no existe el usuraio 
        if User.objects.filter(username = username).exists():
            messages.error(request, "El Usuario ya existe")
            return render(request, "private/crear_usuarios.html")

        #si no existe el correo
        if User.objects.filter(email = email).exists():
            messages.error(request, "El correo ya existe")
            return render(request, "private/crear_usuarios.html")
        
        #crear usuraio 

        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        messages.success(request, "Usuario creado con exito")
        return redirect("listar_usuarios")
    return render(request, "private/crear_usuarios.html")

def eliminar_usuario(request, id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    messages.success(request, "Usuario eliminado")
    return redirect("listar_usuarios")

def editar_usuario(request, id): #metodo editar
    usuario = User.objects.get(id = id)
    if request.method == "POST":
        username = request.POST.get("username_edit")
        email = request.POST.get("email_edit")
        password = request.POST.get("password_edit")

        #Verificar si existe el username
        if User.objects.filter(username = username).exclude(id = id).exists():
            messages.error(request, "El usuario ya esta registrado")
            return render(request, "private/editar_usuario.html", {"usuario":usuario})
        
        #Verificar si existe el email
        if User.objects.filter(email = email).exclude(id = id).exists():
            messages.error(request, "El correo ya existe")
            return render(request, "private/editar_usuario.html", {"usuario":usuario})
        #Actualizar datos

        usuario.username = username
        usuario.email = email
        if password:
            usuario.set_password(password)
            

        usuario.save()
        messages.success(request, "El registro se actualizo con exito")
        return redirect("listar_usuarios")
    contexto = {
        "usuario":usuario
    }
    return render(request, "private/editar_usuario.html", contexto)
    