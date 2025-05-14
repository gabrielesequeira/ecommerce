from flask import request, jsonify
from models import Product, CartItem
from database import db

def configure_routes(app):
    # Rota para listar todos os produtos
    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        result = [{"id": p.id, "name": p.name, "price": p.price, "description": p.description, "category": p.category} for p in products]
        return jsonify(result)

    # Rota para adicionar um produto no carrinho
    @app.route('/cart', methods=['POST'])
    def add_to_cart():
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        
        # Cria o item no carrinho
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()
        
        return jsonify({"message": "Item adicionado ao carrinho!"}), 201

    # Rota para visualizar o carrinho
    @app.route('/cart', methods=['GET'])
    def view_cart():
        cart_items = CartItem.query.all()
        result = [{"product_id": c.product_id, "quantity": c.quantity} for c in cart_items]
        return jsonify(result)
