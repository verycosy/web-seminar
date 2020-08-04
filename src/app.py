from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from bson import ObjectId, json_util
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = "JNU"

client = MongoClient('mongodb://localhost:27017/')
plc_db = client.plc
products = plc_db.products


@app.route('/', methods=['GET'])
def index():
    allProducts = products.find()
    return render_template('index.html', allProducts=list(allProducts))


@app.route('/product', methods=['POST'])
def add_product():
    product = request.get_json()

    newProduct = {'name': product['name'], 'category': product['category']}
    products.insert(newProduct)

    return "add success", 201


@app.route('/product/<string:product_id>', methods=['GET'])
def get_item(product_id):
    product = products.find_one(
        {
            "_id": ObjectId(product_id)  # 코드 규칙
        }
    )

    product = json.loads(json_util.dumps(product))

    return jsonify(product)


if __name__ == '__main__':
    app.run(host="127.0.0.1")
