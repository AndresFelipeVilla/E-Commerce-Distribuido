from rest_framework.routers import DefaultRouter
from .views import StockViewSet

router_inventory = DefaultRouter()
router_inventory.register(prefix='stock', viewset=StockViewSet, basename='stock')

