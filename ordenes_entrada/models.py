from django.db import models
from django.contrib.auth.models import User

class OrdenEntrada(models.Model):
    
    proveedor = models.ForeignKey(
        'proveedores.Proveedor', 
        on_delete=models.CASCADE, 
        verbose_name="Proveedor"
    )
    
    usuario = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        verbose_name="Usuario/Responsable"
    )
    
    fecha_ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de Ingreso")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        return f"Entrada N° {self.id} - Proveedor: {self.proveedor.nombre_empresa}"

    class Meta:
        verbose_name = "Orden de Entrada"
        verbose_name_plural = "Órdenes de Entrada"