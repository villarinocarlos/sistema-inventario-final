from django.db import models

class Inventario(models.Model):
    CATEGORIAS_CHOICES = [
        ('electronica', 'Electrónica'),
        ('hogar', 'Hogar'),
        ('entretenimiento', 'Entretenimiento'),
    ]

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES, null=True, blank=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.nombre
