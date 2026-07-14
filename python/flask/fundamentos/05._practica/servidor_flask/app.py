from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>pagina principal</h1>"

@app.route("/ruta_dinamica/<nombre>/color/<color>")
def color_favorito(nombre, color):
        return f"Hola {nombre}, tu color favorito es {color}"


@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces


@app.route("/despedida/<nombre>")
def despedida(nombre):

    return f"Adios {nombre}!"

@app.route('/<texto_erroneo>')
def ruta_equivocada(texto_erroneo):
    return f"<h1>Error: La sección '{texto_erroneo}' no existe en este sitio.</h1> <p>Por favor, verifica lo que escribiste.</p>", 404


if __name__ == "__main__":
    app.run(debug=True)