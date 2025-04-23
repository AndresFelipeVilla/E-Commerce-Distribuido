from django.db import models
from category.models import Category

class Producto(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['date_created']
        
        
