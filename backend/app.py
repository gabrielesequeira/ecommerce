# arquivo principal do servidor Flash

from flask import flask

app = Flask (__name__)

@app.rout("/")
def home():
    return "ecommerce backend is running"


if __name__== "__main__":
        app.run(debug = True , host = "0.0.0.0")