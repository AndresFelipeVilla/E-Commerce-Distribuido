from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from . utils import get_product_details

from app_inventory.models import Stock
from .serializers import StockSerializer

class StockViewSet(viewsets.GenericViewSet):
    
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'product_id'  # Usando el ID de producto como PK del stock

    
    #accion para verificar stock incluyendo detalles del producto
    @action(detail=True, methods=['get'])
    def check_stock_with_details(self, request, pk=None):
        """
        Verifica la cantidad de stock para un producto e incluye detalles del producto.
        Consulta el servicio de productos para obtener detalles.
        """
        # Obtiene la instancia de Stock usando el pk (que será el product_id de la URL)
        stock_instance = get_object_or_404(Stock, product_id=pk)
        
        # consultar el servicio de productos para obtener detalles del producto
        product_details = get_product_details(pk)
        
        # verificar si se obtuvieron detalles del producto
        if product_details is None:
            return Response({"error": "No se pudo obtener detalles del producto."}, status=status.HTTP_404_NOT_FOUND)
        
        # Usa el serializador para devolver los datos del stock
        serializer = self.get_serializer(stock_instance).data
        
        # convinar los detalles del stock con los detalles de producto
        # Aquí, combinamos los datos de stock y añadimos una clave 'product' con sus detalles.
        response_data = {
            "stock_info": serializer,
            "product_details": product_details
        } 
        
        # Aquí puedes agregar lógica para obtener detalles del producto desde otro servicio si es necesario
        return Response(status=status.HTTP_200_OK, data=response_data)


    # accion para verificar el stock de un producto en especifico
    # 'detail=True' indica que esta acción opera sobre una instancia específica (usando el lookup field)
    @action(detail=True, methods=['get'])
    def check_stock(self, request, pk=None):
        """
        verifica la cantidad de stock para un prodcuto dado su ID"""
        # Obtiene la instancia de Stock usando el pk (que será el product_id de la URL)
        stock_instance = get_object_or_404(Stock, product_id=pk)
        # Usa el serializador para devolver los datos del stock
        serializer = self.get_serializer(stock_instance)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
     
    # accion para aumentar el stock de un producto
    @action(detail=True, methods=['post'])
    def increase_stock(self, request, pk=None):
        """
        Aumenta la cantidad de stock para un producto dado su ID"""
        # Obtiene la instancia de Stock usando el pk (que será el product_id de la URL)
        stock_instance = get_object_or_404(Stock, product_id=pk)
        
        # Espera un JSON con la cantidad a aumentar
        # Ejemplo: { "quantity": 10 }
        increase_amount = request.data.get('quantity')
        
        if increase_amount is None or not isinstance(increase_amount, int) or increase_amount <= 0:
            return Response({"error": "Cantidad inválida para aumentar el stock."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Aumenta la cantidad de stock
        stock_instance.quantity += increase_amount
        stock_instance.save()
        
        # Usa el serializador para devolver los datos del stock actualizado
        serializer = self.get_serializer(stock_instance)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    
    # accion para disminuir el stock de un producto
    @action(detail=True, methods=['post'])
    def decrease_stock(self, request, pk=None):
        """
        Disminuye la cantidad de stock para un producto dado su ID"""
        # Obtiene la instancia de Stock usando el pk (que será el product_id de la URL)
        stock_instance = get_object_or_404(Stock, product_id=pk)
        
        # Espera un JSON con la cantidad a disminuir
        # Ejemplo: { "quantity": 5 }
        decrease_amount = request.data.get('quantity')
        
        if decrease_amount is None or not isinstance(decrease_amount, int) or decrease_amount <= 0:
            return Response({"error": "Cantidad inválida para disminuir el stock."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verifica que no se intente disminuir más de lo que hay en stock
        if decrease_amount > stock_instance.quantity:
            return Response({"error": "No se puede disminuir más de lo que hay en stock."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Disminuye la cantidad de stock
        stock_instance.quantity -= decrease_amount
        stock_instance.save()
        
        # Usa el serializador para devolver los datos del stock actualizado
        serializer = self.get_serializer(stock_instance)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    