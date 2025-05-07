from rest_framework import serializers
from app_producto.models import Producto
from category.api.serializer import CategorySerializer

class ProductoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Producto
        fields = ['id', 'name', 'description', 'price', 'category']
        
        

        