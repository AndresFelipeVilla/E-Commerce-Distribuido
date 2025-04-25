from django.db import models
from django.core.validators import MinValueValidator

class Stock(models.Model):
    
    product_id = models.IntegerField(primary_key=True) # Usando el ID de producto como PK del stock
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='cantidad actual en stock')
    date_created = models.DateTimeField(auto_now_add=True, help_text='fecha de creación del stock')
    date_updated = models.DateTimeField(auto_now=True, help_text='fecha de actualización del stock')
    
    def __str__(self):
        return f"Stock para el Producto ID {self.product_id}: {self.quantity} unidades"
    
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['product_id'] 

