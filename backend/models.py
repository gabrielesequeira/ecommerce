# models.py
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) #Ligado a tabela de product
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Ligado a tebela de User
    product = db.relationship('Product', backref='cart_items') # objeto python para consulta de seus atributos product.name
    user = db.relationship('User', backref='cart_items')  # objeto python para consulta tbm

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # será uma hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # Criptografa a senha

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # Verifica a senha
# Esta classe representa um usuário no sistema, com:
# - email único (login)
# - senha criptografada com hash (segurança)
# - métodos para salvar/verificar senha com segurança (sem guardar senha pura!)
