from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
   session["nombre"] = request.form.get("nombre", "").strip()
   session["edad"] = request.form.get("edad", "").strip()
   session["color"] = request.form.get("color", "").strip()
   session["animal"] = request.form.get("animal", "").strip()
   return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
   if "nombre" not in session:
      return redirect(url_for("index"))

   mensajes = [
      "Un cambio inesperado abrirá una oportunidad importante para ti.",
      "Una nueva aventura llegará cuando menos lo esperes.",
      "La constancia te llevará más lejos de lo que imaginas.",
      "Alguien especial aparecerá para compartir un momento memorable.",
   ]
   return render_template("futuro.html", datos=session, mensaje=random.choice(mensajes))

if __name__ == "__main__":
   app.run(debug=True)
