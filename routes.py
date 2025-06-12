from flask import Blueprint, render_template, request
#blueprint - permite separar as rotas do app principal
#render_templates - renderiza arquivos HTML
#request - permite acessar dados enviados pelo usuário

myblue = Blueprint('routes', __name__) #cria o grupo de rotas

@myblue.route('/')
def home():
    return render_template('inicio.html')


@myblue.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        enviado = True #msg enviada
    return render_template('contato.html', enviado=False)
    # Se for apenas GET (acesso comum), mostra o formulário normalmente


@myblue.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@myblue.route('/produtos')
def produtos():
    return render_template('produtos.html')

@myblue.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')