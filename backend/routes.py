# rotas da API

# backend/routes.py
from flask import Flask, jsonify, request
from backend.models import db, Product, Cart

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@app.route('/api/cart', methods=['GET'])
def get_cart():
    cart_items = Cart.query.all()
    return jsonify([{'product': item.product.name, 'quantity': item.quantity} for item in cart_items])

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    user_id = 1  # Para simplificação, vamos fixar o ID do usuário como 1

    product = Product.query.get(product_id)
    if product:
        cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
        db.session.commit()
        return jsonify({'message': 'Produto adicionado ao carrinho!'}), 200
    else:
        return jsonify({'message': 'Produto não encontrado!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
