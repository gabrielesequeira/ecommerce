# vamos usar o framework flask do python para desenvolvimento web

from flask import Flask 
#importar a principal classe 
from routes import myblue 
#importa o blueprint que foi criado em routes.py

app = Flask(__name__) # o site criado pela definição de aplicação , é o arquivo principal
app.register_blueprint(myblue) # dividir rotas do app em aquivo separado (routes.py)




if __name__ == '__main__':
    app.run(debug=True)  # só vai rodar esse código se rodar o arquivo todo se estiver importando n vai 
