from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    return render_template("index.html",
    nombre ="Martin", curso ="4C", 
    ciudad ="Santiago", anio ="2026",
    profesor =False, 
      tecnologias=[
          
        "Python",

        "Flask",

        "HTML",

        "CSS"

    ])
@app.route("/jugador")
def jugador():

    return render_template("jugador.html",
    jugador="kagekaoo",

    puntaje=3600,

    lider=True
)

    
if __name__ == "__main__":

    app.run(debug=True)
