from rest_framework import serializers
from app_inventory.models import Stock

class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Stock
        fields = ['product_id', 'quantity', 'date_created', 'date_updated']
        read_only_fields = ['id', 'date_created', 'date_updated'] 
        
