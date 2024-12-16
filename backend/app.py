# arquivo principal do servidor Flash

from flask import Flask
from flask_cors import CORS

app = Flask (__name__)

@app.route("/")
def home():
    return "ecommerce backend is running"


if __name__== "__main__":
    app.run(debug = True , host = "0.0.0.0")


app = Flask(__name__)
CORS(app)

@app.route("/api/products")
def get_products():
    return {"products": ["Laptop", "Smartphone", "Tablet"]}
