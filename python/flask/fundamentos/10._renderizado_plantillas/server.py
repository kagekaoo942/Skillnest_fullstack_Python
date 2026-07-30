from flask import Flask, render_template

app = Flask(__name__)


#Ruta 1
@app.route("/listas")
def renderizar_listas():

    # Lista de números
    numeros = [7, 15, 22]

    # Lista de diccionarios
    listado_estudiantes = [
        {"nombre": "Florencia", "edad": 25},
        {"nombre": "Valentina", "edad": 30},
        {"nombre": "José", "edad": 27},
        {"nombre": "Patricio", "edad": 21},
    ]

    return render_template(
        "listas.html", numeros=numeros, estudiantes=listado_estudiantes
    )


#Ruta 2
@app.route("/videojuegos")
def renderizar_videojuegos():
    lista_videojuegos = [
        {"nombre": "Minecraft", "plataforma": "PC", "anio": 2011},
        {
            "nombre": "The Legend of Zelda: BOTW",
            "plataforma": "Nintendo Switch",
            "anio": 2017,
        },
        {"nombre": "God of War", "plataforma": "PlayStation 4", "anio": 2018},
        {"nombre": "Halo Infinite", "plataforma": "Xbox Series X", "anio": 2021},
        {"nombre": "Elden Ring", "plataforma": "PC", "anio": 2022},
        {"nombre": "Grand Theft Auto V", "plataforma": "Multiplataforma", "anio": 2013},
    ]

    return render_template("videojuegos.html", juegos=lista_videojuegos)
if __name__ == "__main__":
    app.run(debug=True)