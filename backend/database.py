#configuração do banco de dados

#O SQLAlchemy é um ORM (Object-Relational Mapper), que traduz tabelas do banco de dados
#em objetos Python. Isso simplifica operações como consultas e atualizações no banco.



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
