from django.db import models

class Lote(models.Model):
    
    producto = models.ForeignKey(
        'productos.Producto', 
        on_delete=models.CASCADE, 
        verbose_name="Producto Asociado"
    )
    
    fecha_fabricacion = models.DateField(verbose_name="Fecha de Fabricación")
    fecha_caducidad = models.DateField(verbose_name="Fecha de Caducidad")
    cantidad_inicial = models.IntegerField(verbose_name="Cantidad Inicial del Lote")

    def __str__(self):
        return f"Lote {self.id} - {self.producto.nombre}"

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"