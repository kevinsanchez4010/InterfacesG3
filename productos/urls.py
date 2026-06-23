from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),

    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name ="eliminar_producto"),
    path('editar_usuario/<int:id>/', views.editar_producto, name = "editar_producto")

]