from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.models.restaurante import Restaurante
from flask_app.models.taco import Taco


@app.route("/")
def index():
    """Muestra el formulario para crear un taco y elegir restaurante."""
    return render_template(
        "index.html",
        todos_restaurantes=Restaurante.get_all()
    )


@app.route("/crear", methods=["POST"])
def crear():
    """Valida el formulario, guarda el taco y vuelve al listado."""
    datos = {
        "tortilla": request.form.get("tortilla", "").strip(),
        "guiso": request.form.get("guiso", "").strip(),
        "salsa": request.form.get("salsa", "").strip(),
        "restaurante_id": request.form.get("restaurante_id", "").strip()
    }

    if not all(datos.values()):
        return render_template(
            "index.html",
            todos_restaurantes=Restaurante.get_all(),
            datos=datos,
            error="Completa todos los campos y selecciona un restaurante."
        ), 400

    resultado = Taco.save(datos)
    if resultado is False:
        return render_template(
            "index.html",
            todos_restaurantes=Restaurante.get_all(),
            datos=datos,
            error="No fue posible guardar el taco. Verifica el restaurante."
        ), 500

    return redirect(url_for("tacos"))


@app.route("/tacos")
def tacos():
    """Lista los tacos creados y enlaza cada uno con su restaurante."""
    return render_template("index.html", tacos=Taco.get_all())


@app.route("/restaurantes/<int:id>")
def restaurante(id):
    """Muestra un restaurante con los tacos relacionados."""
    restaurante_encontrado = Restaurante.get_restaurante_y_tacos({"id": id})
    if restaurante_encontrado is None:
        return "Restaurante no encontrado", 404

    return render_template(
        "restaurante.html",
        restaurante=restaurante_encontrado
    )


@app.route("/restaurantes")
def restaurantes():
    """Muestra todos los restaurantes."""
    return render_template(
        "restaurantes.html",
        restaurantes=Restaurante.get_all()
    )
