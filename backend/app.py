from flask import Flask, render_template
from routes import configure_routes
from database import db
from flask_cors import CORS
from flask_login import LoginManager
from models import User  

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

#Chave secreta para sessões:
app.secret_key = 'segredo-super-seguro-da-bê'


#configurando usuário
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # redirecionamento padrão

# Callback para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





if __name__ == '__main__':
    app.run(debug=True)
