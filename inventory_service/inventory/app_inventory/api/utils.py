
import requests
import os

# URL base del servicio de productos dentro de la red Docker
# Usamos el nombre del servicio 'producto-service' como hostname
# y el puerto interno 8000.
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://producto_service:8000/api/product")

def get_product_details(product_id):
    """
    Consulta el servicio de productos para obtener los detalles de un producto.

    Args:
        product_id: El ID entero del producto a consultar.

    Returns:
        Un diccionario con los detalles del producto si se encuentra (status 200).
        None si el producto no se encuentra (status 404) o si hay otro error.
    """
    # construye la URL para la consulta
    url = f"{PRODUCT_SERVICE_URL}/{product_id}/"
    
    try:
        # realiza la consulta al servicio de productos
        response = requests.get(url)
        
        # verifica el código de estado de la respuesta
        if response.status_code == 200:
            return response.json()  # devuelve los detalles del producto
        elif response.status_code == 404:
            print(f"Producto con ID {product_id} no encontrado en product_service.")
            return None  # producto no encontrado
        else:
            # Manejar otros posibles errores (400, 500, etc.)
            print(f"Error al consultar product_service para ID {product_id}: Status {response.status_code}")
            print(f"Respuesta del error: {response.text}")
            return None
        
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión o tiempo de espera
        print(f"Error de conexión al consultar product_service: {e}")
        return None
        