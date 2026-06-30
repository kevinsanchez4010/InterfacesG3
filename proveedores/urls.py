from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('editar_proveedor/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
]