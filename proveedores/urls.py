from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_proveedores, Nombre='listar_proveedores'),
    path('crear_proveedor/', views.crear_proveedor, Nombre='crear_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminar_proveedor, Nombre='eliminar_proveedor'),
    path('editar_proveedor/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
]