from django_filters.rest_framework import FilterSet
import django_filters
from app_producto.models import Producto

class ProductoFilter(FilterSet):
    
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')
    
    class Meta:
        model = Producto
        fields = {
            'name': ['exact', 'icontains'],  # Permite exacto o icontains
            'price': ['exact', 'lt', 'gt', 'lte', 'gte'], # Permite exacto, menor que, mayor que, etc.
            'category': ['exact', 'iexact'], # Permite exacto o iexact
            
        }