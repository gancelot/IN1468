"""
    acquire_product_info.py
    In order to use this, the server in app.py within the api directory must be running first.
"""
import json
import requests


base_url = 'http://localhost:8000/api/products'


def get_product_info(product_id: int = 0) -> dict:
    """
    Fetches product information from the API.

    Args:
        product_id (int): The ID of the product to fetch. Defaults to 0, which fetches all products.

    Returns:
        dict: The response data from the API in JSON format.
    """
    
    url = base_url
    if product_id:
        url = f'{base_url}/{product_id}'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    products = get_product_info()
    for product in products.get('results'):
        print(json.dumps(product, indent=4))
