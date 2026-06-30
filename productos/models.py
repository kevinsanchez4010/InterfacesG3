from django.db import models

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    ubicacion = models.ForeignKey(
        'Ubicacion', 
        on_delete=models.PROTECT, 
        verbose_name="Ubicación en Bodega"
    )
    
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Costo")
    stock_actual = models.IntegerField(verbose_name="Stock Disponible")
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='activo', 
        verbose_name="Estado del Producto"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
