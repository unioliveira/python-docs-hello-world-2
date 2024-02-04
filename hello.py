from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    returan "Hello, World! - Atualização"
