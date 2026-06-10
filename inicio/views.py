from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

# Create your views here.

def hola(request):
    return render(request, 'index.html')

def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, 
                            username=username, 
                            password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    return render(request, 'login.html', {'mensaje': mensaje})

def dashboard(request):
    return render(request, 'dashboard.html')