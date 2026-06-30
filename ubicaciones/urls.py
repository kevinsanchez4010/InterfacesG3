from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ubicaciones, name='listar_ubicaciones'),
    
    path('crear_ubicacion/', views.crear_ubicacion, name="crear_ubicacion"),
    path('eliminar_ubicacion/<int:id>/', views.eliminar_ubicacion, name="eliminar_ubicacion"),
    path('editar_ubicacion/<int:id>/', views.editar_ubicacion, name="editar_ubicacion"),
]