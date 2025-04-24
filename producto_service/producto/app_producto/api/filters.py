import django_filters
from app_producto.models import Producto

class ProductoFilter(django_filters.rest_framework.FilterSet):
    
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = django_filters.RangeFilter(field_name='price')
    
    class Meta:
        model = Producto
        fields = {
            'name': ['exact', 'icontains'], # Permite exacto o icontains
            'category__slug': ['exact', 'iexact', 'icontains'], # Permite exacto o iexact
            'price': ['lt', 'gt', 'lte', 'gte'], # Permite exacto, menor que, mayor que, etc.
        }