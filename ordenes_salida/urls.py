from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ordenes_salida, name='listar_ordenes_salida'),
    path('crear_orden_salida/', views.crear_orden_salida, name='crear_orden_salida'),
    path('eliminar_orden_salida/<int:id>/', views.eliminar_orden_salida, name='eliminar_orden_salida'),
    path('editar_orden_salida/<int:id>/', views.editar_orden_salida, name='editar_orden_salida'),
]
