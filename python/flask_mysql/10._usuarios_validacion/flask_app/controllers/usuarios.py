from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    """Redirige la raíz al listado de usuarios."""
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    """Carga el listado de usuarios registrados."""
    return render_template("usuarios.html", usuarios=Usuario.get_all())


@app.route("/usuarios/nuevo")
def nuevo_usuario():
    """Muestra el formulario y consume datos temporales de la sesión."""
    datos_formulario = session.pop("datos_formulario", {})
    return render_template(
        "nuevo_usuario.html",
        datos_formulario=datos_formulario,
    )


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    """Valida los datos antes de comprobar unicidad y guardar."""
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip(),
    }

    if not Usuario.validar_usuario(data):
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))

    if Usuario.email_existe(data["email"]):
        flash("El email ingresado ya está registrado.", "email")
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))

    resultado = Usuario.save(data)
    if resultado is False:
        flash("No fue posible crear el usuario.", "error")
        session["datos_formulario"] = data
        return redirect(url_for("nuevo_usuario"))

    session.pop("datos_formulario", None)
    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("usuarios"))
