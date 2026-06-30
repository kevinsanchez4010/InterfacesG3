from django.db import models
from django.contrib.auth.models import User


class OrdenSalida(models.Model):
    
    producto = models.ForeignKey(
        'productos.Producto', 
        on_delete=models.CASCADE, 
        verbose_name="Producto Despachado"
    )
    
    usuario = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        verbose_name="Usuario/Responsable"
    )
    
    cantidad_salida = models.IntegerField(verbose_name="Cantidad a Retirar")
    fecha_salida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de Salida")

    def __str__(self):
        return f"Salida N° {self.id} - {self.producto.nombre} ({self.cantidad_salida} unds)"

    class Meta:
        verbose_name = "Orden de Salida"
        verbose_name_plural = "Órdenes de Salida"