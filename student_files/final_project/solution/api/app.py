"""
    app.py
    This file defines the Flask application and its routes.
    It runs on port 8000 by default.
    It must be started first in order to test it.
    Test it by visiting http://localhost:8000/api/products and
    http://localhost:8000/api/products/2001.
"""
from pathlib import Path
from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

db_location = Path(__file__).parents[2] / 'resources/product_data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_location)
app.config['SQLALCHEMY_ECHO'] = True
print(f'Using database location: {r"sqlite:///" + str(db_location)}')

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    """
    Represents a product in the database.

    Attributes:
        product_id (int): The unique identifier of the product.
        name (str): The name of the product.
        description (str): A short description of the product.
        category (str): The category to which the product belongs.
        price (float): The price of the product.
        stock_quantity (int): The quantity of the product available in stock.
        color (str): The color of the product.
        weight (str): The weight of the product.
        dimensions (str): The dimensions of the product.
    """
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    color = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    dimensions = db.Column(db.String(100))

    def __init__(self, name, description, category, price, stock_quantity, color, weight, dimensions):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
        self.color = color
        self.weight = weight
        self.dimensions = dimensions


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> tuple[Response, int]:
    """
    Retrieve a product by its ID.

    Args:
        product_id (int): The unique identifier of the product to retrieve.

    Returns:
        Response: A JSON response containing the product's information
                  if found, or an error message if not found.
    """
    
    try:
        product = db.session.get(Product, product_id)
        if not product:
            results = ['Product not found.']
            status = 400
        else:
            results = product_schema.dump(product)
            status = 200
    except SQLAlchemyError as err:
        results = err.args
        status = 404

    return jsonify(results=results), status


@app.route('/api/products', methods=['GET'])
def get_all_products() -> tuple[Response, int]:
    try:
        stmt = db.select(Product)
        products = db.session.scalars(stmt).all()
        if not products:
            results = ['No results found.']
            status = 400
        else:
            results = product_schema_many.dump(products)
            status = 200
    except SQLAlchemyError as err:
        results = err.args
        status = 404

    return jsonify(results=results), status


class ProductSchema(ma.Schema):
    """
    A Marshmallow schema for serializing and deserializing Product objects.

    This schema maps the attributes of the Product model to JSON format,
    facilitating easy conversion between database objects and API responses.
    """
    
    class Meta:
        fields = ('product_id', 'name', 'description', 'category',
                  'price', 'stock_quantity', 'color', 'weight', 'dimensions')


product_schema = ProductSchema()
product_schema_many = ProductSchema(many=True)

app.run(host='localhost', port=8000)
