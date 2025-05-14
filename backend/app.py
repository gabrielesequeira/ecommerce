from flask import Flask, render_template
from routes import configure_routes
from database import db
from flask_cors import CORS

# Inicializar o app Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o banco de dados
db.init_app(app)

# Configurar o CORS
CORS(app)

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Configurar as rotas
configure_routes(app)

# Rota para servir o frontend
@app.route('/')
def index():
    return render_template('index.html')  # Esta linha garante que o index.html seja servido

if __name__ == '__main__':
    app.run(debug=True)
