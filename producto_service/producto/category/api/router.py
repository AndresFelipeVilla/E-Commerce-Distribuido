from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router_category = DefaultRouter()
router_category.register(prefix='category', viewset=CategoryViewSet, basename='category')