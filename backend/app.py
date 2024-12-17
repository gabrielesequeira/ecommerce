from flask import Flask
from routes import configure_routes
from database import db

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o banco de dados
db.init_app(app)

# Configurar as rotas
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
