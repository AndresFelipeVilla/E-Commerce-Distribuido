from django.db import models

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']