from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

MENSAJES_DESTINO = [
   "Un cambio inesperado abrirá una oportunidad importante para ti.",
   "Una nueva aventura llegará cuando menos lo esperes.",
   "La constancia te llevará más lejos de lo que imaginas.",
   "Alguien especial aparecerá para compartir un momento memorable.",
   "Tendrás algunos obstáculos, pero aprenderás mucho de esta etapa.",
   "Un plan podría no salir como esperabas; mantén la calma y vuelve a intentarlo.",
   "Cuidado con tomar decisiones apresuradas durante los próximos días.",
   "Una pequeña decepción te ayudará a descubrir lo que realmente quieres.",
]

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
   nombre = request.form.get("nombre", "").strip()
   edad = request.form.get("edad", "").strip()
   color = request.form.get("color", "").strip()
   animal = request.form.get("animal", "").strip()

   if not all([nombre, edad, color, animal]):
      return redirect(url_for("index"))

   session["nombre"] = nombre
   session["edad"] = edad
   session["color"] = color
   session["animal"] = animal
   session["numero_suerte"] = random.randint(1, 99)
   session["mensaje"] = random.choice(MENSAJES_DESTINO)
   colores = {
      "rojo": "color-rojo",
      "azul": "color-azul",
      "verde": "color-verde",
      "morado": "color-morado",
      "amarillo": "color-amarillo",
      "naranja": "color-naranja",
      "rosa": "color-rosa",
      "blanco": "color-blanco",
      "negro": "color-negro",
   }
   session["color_class"] = colores.get(color.lower(), "color-verde")
   return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
   if "nombre" not in session:
      return redirect(url_for("index"))

   return render_template(
      "futuro.html",
      datos=session,
      mensaje=session["mensaje"],
      color_class=session.get("color_class", "color-verde"),
      numero_suerte=session.get("numero_suerte", random.randint(1, 99))
   )

if __name__ == "__main__":
   app.run(debug=True)
