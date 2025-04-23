from django.contrib import admin
from . models import Producto, Category

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category__name', 'date_created')
    search_fields = ('name',)
