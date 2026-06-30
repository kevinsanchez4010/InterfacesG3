from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lotes, name='listar_lotes'),
    
    path('crear_lote/', views.crear_lote, name="crear_lote"),
    path('eliminar_lote/<int:id>/', views.eliminar_lote, name ="eliminar_lote"),
    path('editar_lote/<int:id>/', views.editar_lote, name = "editar_lote")
    
]