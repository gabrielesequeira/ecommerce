# arquivo principal do servidor Flash

# backend/app.py
from backend.models import db, Product
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def setup():
    db.create_all()
    if not Product.query.first():
        products = [
            Product(name="Produto 1", price=100),
            Product(name="Produto 2", price=150),
            Product(name="Produto 3", price=200)
        ]
        db.session.add_all(products)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
