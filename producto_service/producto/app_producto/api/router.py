from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Crear un enrutador y registrar el ProductViewSet
router_producto = DefaultRouter()
router_producto.register(prefix='product', basename='product', viewset=ProductoViewSet)