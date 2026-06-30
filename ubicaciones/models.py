from django.db import models

class Ubicacion(models.Model):
    ESTADO_ESPACIO_CHOICES = [
        ('disponible', 'Disponible'),
        ('lleno', 'Lleno'),
        ('mantenimiento', 'En Mantenimiento'),
    ]

    nombre_area = models.CharField(max_length=100, verbose_name="Nombre del Área / Zona")
    capacidad_maxima = models.IntegerField(verbose_name="Capacidad Máxima (Unidades)")
    seccion_fila = models.CharField(max_length=100, verbose_name="Sección y Fila (Coordenadas)")
    estado_espacio = models.CharField(
        max_length=20, 
        choices=ESTADO_ESPACIO_CHOICES, 
        default='disponible', 
        verbose_name="Estado del Espacio"
    )

    def __str__(self):
        return f"{self.nombre_area} - {self.seccion_fila}"

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"