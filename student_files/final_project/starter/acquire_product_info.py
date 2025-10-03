"""
    acquire_product_info.py
    In order to use this, the server in app.py within the api directory must be running first.
"""
import json
import requests


base_url = 'http://localhost:8000/api/products'

# Step 7. Retrieve a single product if a product_id is provided, otherwise retrieve
# all products.  Use the requests.get() method to help accomplish this.  Refer to app.py
# for the URLs, however, this file can test itself by running it directly.  This is because
# there is a test script down at the bottom of this file that should work when you finish
# creating this method.
def get_product_info(product_id: int = 0) -> dict:
    pass


if __name__ == '__main__':
    products = get_product_info()
    for product in products.get('results'):
        print(json.dumps(product, indent=4))
