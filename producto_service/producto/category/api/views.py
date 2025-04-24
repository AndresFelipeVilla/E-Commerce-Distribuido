from rest_framework.viewsets import ModelViewSet
from .serializer import CategorySerializer
from category.models import Category
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
    