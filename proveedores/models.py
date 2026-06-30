from django.db import models

class Proveedor(models.Model):
    
    nombre_empresa = models.CharField(max_length=200, verbose_name="Nombre de la Empresa / Razón Social")
    ruc_proveedor = models.CharField(max_length=13, unique=True, verbose_name="RUC del Proveedor")
    telefono_contacto = models.CharField(max_length=15, verbose_name="Teléfono de Contacto")
    direccion_matriz = models.TextField(verbose_name="Dirección Matriz")

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"