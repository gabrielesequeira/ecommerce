from flask import request, jsonify
from models import Product, CartItem
from database import db
from models import Product, CartItem, User
from flask import session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash





def configure_routes(app):
    # Rota para listar todos os produtos
    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        result = [{"id": p.id, "name": p.name, "price": p.price, "description": p.description, "category": p.category} for p in products]
        return jsonify(result)

    @app.route('/cart', methods=['POST'])
    @login_required
    def add_to_cart():
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        cart_item = CartItem(product_id=product_id, quantity=quantity, user_id=current_user.id)
        db.session.add(cart_item)
        db.session.commit()

        return jsonify({"message": "Item adicionado ao carrinho!"}), 201


    @app.route('/cart', methods=['GET'])
    @login_required
    def view_cart():
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        result = [
            {
                "product_id": c.product_id,
                "quantity": c.quantity,
                "product_name": c.product.name,
                "price": c.product.price
            } for c in cart_items
        ]
        return jsonify(result)



    # REGISTRO
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Usuário já existe'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuário registrado com sucesso!"}), 201
# /register:
# - Verifica se o email já existe
# - Cria novo usuário com senha criptografada
# - Salva no banco


    # LOGIN
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"message": "Credenciais inválidas"}), 401
        
        login_user(user)
        return jsonify({"message": "Login realizado com sucesso!"})

# /login:
# - Busca o usuário pelo email
# - Verifica se a senha está correta usando hash
# - Retorna sucesso ou erro

    # LOGOUT
    @app.route('/logout', methods=['POST'])
    @login_required
    def logout():
        logout_user()
        return jsonify({"message": "Logout realizado com sucesso!"})
