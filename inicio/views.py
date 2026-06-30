from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages  # <-- Importamos esto para el mensaje de éxito


def hola(request):
    return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    mensaje = ''

    if User.objects.count() == 0:
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin1234')
        messages.info(request, 'Usuario por defecto creado: admin / Admin1234')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            
            messages.success(request, "Datos correctos")
            return redirect('dashboard')
        else:
            mensaje = 'Datos incorrectos'
            
    return render(request, 'login.html', {'mensaje': mensaje})
