from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock Disponible")

    def __str__(self):
        return self.nombre
