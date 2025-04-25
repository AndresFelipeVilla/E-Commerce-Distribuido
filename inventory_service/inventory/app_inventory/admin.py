from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'quantity', 'date_created', 'date_updated')
    search_fields = ('product_id',)
    list_filter = ('date_created', 'date_updated')
    ordering = ('product_id',)
    date_hierarchy = 'date_created'
    list_per_page = 20
