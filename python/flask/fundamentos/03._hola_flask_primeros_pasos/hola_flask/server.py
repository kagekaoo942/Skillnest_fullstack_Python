from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola a todos!"

@app.route("/nosotros")
def nosotros():
    return "<h1 ¡Conócenos un poco más!</h1>"

@app.route("/contacto")
def contacto():
    return "<h1 Nuestro contacto</h1>"

@app.route("/productos")
def productos():
    return "<h1 nuestros productos</h1>"

if __name__ == "__main__":
    app.run(debug=True)