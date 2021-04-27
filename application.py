from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hola FIAP, muito legal é issoooo aeeee!</h1>\nMBA! o/"
