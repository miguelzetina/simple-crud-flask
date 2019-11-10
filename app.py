from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://simple_flask:pass_simple_flask@localhost:5432/simple_crud_flask'
db = SQLAlchemy(app)

# Models
class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(100))
    brand = db.Column(db.String(50))
    price = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, description, brand, price):
        self.title = title
        self.description = description
        self.brand = brand
        self.price = price

    def __repr__(self):
        return '' % self.id

db.create_all()


class ProductSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session

    id = fields.Number(strict=True, dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Number(required=True)


@app.route('/products/', methods = ['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    get_product = Product.query.get(id)
    if data.get('title'):
        get_product.title = data['title']
    if data.get('description'):
        get_product.description = data['description']
    if data.get('brand'):
        get_product.brand = data['brand']
    if data.get('price'):
        get_product.description = data['price']
    db.session.add(get_product)
    db.session.commit()
    product_schema = ProductSchema(only=['id', 'title', 'description','brand','price'])
    product = product_schema.dump(get_product)
    return make_response(jsonify(product))


@app.route('/products', methods = ['GET'])
def index():
    get_products = Product.query.all()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify(products))


@app.route('/products', methods = ['POST'])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema()
    product = product_schema.load(data)
    result = product_schema.dump(product.create())
    return make_response(jsonify(result),200)


@app.route('/products/', methods = ['DELETE'])
def delete_product_by_id(id):
    get_product = Product.query.get(id)
    db.session.delete(get_product)
    db.session.commit()
    return make_response("",204)


@app.route('/products/', methods = ['GET'])
def get_product_by_id(id):
    get_product = Product.query.get(id)
    product_schema = ProductSchema()
    product = product_schema.dump(get_product)
    return make_response(jsonify(product))


if __name__ == "__main__":
    app.run(debug=True)
