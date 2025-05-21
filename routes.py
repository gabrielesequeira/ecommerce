from flask import Blueprint, render_template, request
#blueprint - permite separar as rotas do app principal
#render_templates - renderiza arquivos HTML
#request - permite acessar dados enviados pelo usuário

myblue = Blueprint('routes', __name__) #cria o grupo de rotas

@myblue.route('/')
def home():
    return render_template('index.html')

@myblue.route('/sobre')
def sobre():
    return render_template('sobre.html')

@myblue.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        mensagem = request.form.get('mensagem')
        # Aqui poderia salvar no banco, mas vamos só exibir no console
        print(f"Mensagem recebida de {nome}: {mensagem}")
        return render_template('contato.html', enviado=True)
    return render_template('contato.html', enviado=False)
