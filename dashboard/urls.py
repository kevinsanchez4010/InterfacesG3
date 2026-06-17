from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),

    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name ="eliminar_usuario"),

]
