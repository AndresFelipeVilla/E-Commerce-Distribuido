from rest_framework import serializers
from app_producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Producto
        fields = ['id', 'name', 'description', 'price', 'category']
        
        

        