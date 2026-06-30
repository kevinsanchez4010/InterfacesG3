from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ordenes_entrada, name='listar_ordenes_entrada'),
    path('crear_orden_entrada/', views.crear_orden_entrada, name='crear_orden_entrada'),
    path('eliminar_orden_entrada/<int:id>/', views.eliminar_orden_entrada, name='eliminar_orden_entrada'),
    path('editar_orden_entrada/<int:id>/', views.editar_orden_entrada, name='editar_orden_entrada'),
]
