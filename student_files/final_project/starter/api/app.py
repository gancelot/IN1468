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

# Step 1. Connect the SQLAlchemy plugin and Marshmallow plugins to Flask.
# Refer to class notes on how to do this or view the capstone project solution.


# Step 2. Create the Product SQLAlchemy model class.  The table
# to use is in the resources/product_data.db file and is called "products".
# These are the fields to model: product_id (int), name (str), description (str)
# category (str), price (float), stock_quantity (int), color (str), weight (str),
# dimensions (str).  Add an appropriate __init__() for the class as well.
class Product(db.Model):
    pass


# Step 3. Complete the route() decorator which receives HTTP GET requests.
# This function accept a product id.  It should retrieve the product using
# db.session.get(Table, id).  It should jsonify and return those results.
# The URL mapping is:  '/api/products/<int:product_id>' or something similar to this.
# It should handle HTTP GET requests.
@app.route()
def get_product(product_id):
    pass


# Step 4. Repeat the route() decorator this time for responding to requests
# for ALL products.  This should use the following SQLAlchemy statement:
# db.session.scalars(db.select(Product)).all() to retrieve all products.
@app.route()
def get_all_products():
    pass


# Step 5. Create a schema using the Marshmallow plugin for Flask called ProductSchema.
# It will define a nested class, called Meta, that contains a fields = () tuple with
# all of the fields for a product including the product_id.  Refer to either the solution
# or the class notes on how to do this:
class ProductSchema(ma.Schema):
    pass


product_schema = ProductSchema()
product_schema_many = ProductSchema(many=True)

app.run(host='localhost', port=8000)
