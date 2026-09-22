from flask import redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.taco import Taco


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crear", methods=["POST"])
def crear():
    datos = {
        "tortilla": request.form["tortilla"].strip(),
        "guiso": request.form["guiso"].strip(),
        "salsa": request.form["salsa"].strip(),
    }

    if not all(datos.values()):
        return render_template(
            "index.html",
            error="Todos los campos son obligatorios.",
            datos=datos,
        ), 400

    if Taco.save(datos) is False:
        return render_template(
            "index.html",
            error="No fue posible crear el taco.",
            datos=datos,
        ), 500

    return redirect(url_for("tacos"))


@app.route("/tacos")
def tacos():
    return render_template("resultados.html", todos_tacos=Taco.get_all())


@app.route("/mostrar/<int:taco_id>")
def detalle(taco_id):
    taco = Taco.get_one({"id": taco_id})
    if taco is None:
        return "Taco no encontrado", 404
    return render_template("detalle.html", taco=taco)


@app.route("/editar/<int:taco_id>")
def editar(taco_id):
    taco = Taco.get_one({"id": taco_id})
    if taco is None:
        return "Taco no encontrado", 404
    return render_template("editar.html", taco=taco)


@app.route("/actualizar/<int:taco_id>", methods=["POST"])
def actualizar(taco_id):
    datos = {
        "id": taco_id,
        "tortilla": request.form["tortilla"].strip(),
        "guiso": request.form["guiso"].strip(),
        "salsa": request.form["salsa"].strip(),
    }

    if not all((datos["tortilla"], datos["guiso"], datos["salsa"])):
        taco = Taco.get_one({"id": taco_id})
        return render_template(
            "editar.html",
            taco=taco,
            error="Todos los campos son obligatorios.",
        ), 400

    if Taco.update(datos) is False:
        taco = Taco.get_one({"id": taco_id})
        return render_template(
            "editar.html",
            taco=taco,
            error="No fue posible actualizar el taco.",
        ), 500

    return redirect(url_for("detalle", taco_id=taco_id))


@app.route("/borrar/<int:taco_id>")
def borrar(taco_id):
    if Taco.get_one({"id": taco_id}) is None:
        return "Taco no encontrado", 404

    if Taco.delete({"id": taco_id}) is False:
        return "No fue posible eliminar el taco.", 500

    return redirect(url_for("tacos"))
