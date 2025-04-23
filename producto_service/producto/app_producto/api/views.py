from rest_framework.viewsets import ModelViewSet
from .serializer import ProductoSerializer
from app_producto.models import Producto
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductoFilter

class ProductoViewSet(ModelViewSet):
    
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter
    
    