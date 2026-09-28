import re

from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.seguidor import Seguidor
from flask_app.models.usuario import Usuario


EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def _volver_a_usuarios():
    return redirect(url_for("usuarios"))


@app.route("/")
def inicio():
    """Dirige la ruta principal a la pantalla de administración."""
    return _volver_a_usuarios()


@app.route("/usuarios")
def usuarios():
    """Renderiza usuarios, relaciones y los dos formularios de la vista."""
    lista_usuarios = Usuario.get_all()
    relaciones = Seguidor.get_all()

    if lista_usuarios is None or relaciones is None:
        flash(
            "No fue posible cargar los datos. Revisa la conexión a MySQL.",
            "danger",
        )

    return render_template(
        "usuarios.html",
        usuarios=lista_usuarios or [],
        relaciones=relaciones or [],
    )


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    """Valida y registra un usuario enviado desde el formulario."""
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()

    if not nombre or not apellido or not email:
        flash("Todos los campos son obligatorios.", "danger")
        return _volver_a_usuarios()

    if len(nombre) > 45 or len(apellido) > 45 or len(email) > 45:
        flash("Los campos no pueden superar los 45 caracteres.", "danger")
        return _volver_a_usuarios()

    if not EMAIL_PATTERN.fullmatch(email):
        flash("Introduce una dirección de e-mail válida.", "danger")
        return _volver_a_usuarios()

    resultado = Usuario.save(
        {"nombre": nombre, "apellido": apellido, "email": email}
    )

    if resultado is False:
        flash("No fue posible crear el usuario. Revisa la conexión a MySQL.", "danger")
        return _volver_a_usuarios()

    flash("Usuario creado correctamente.", "success")
    return _volver_a_usuarios()


@app.route("/seguir", methods=["POST"])
def seguir():
    """Registra que seguidor_id sigue a usuario_id."""
    usuario_id_texto = request.form.get("usuario_id", "").strip()
    seguidor_id_texto = request.form.get("seguidor_id", "").strip()

    if not usuario_id_texto or not seguidor_id_texto:
        flash("Debes seleccionar un usuario y un seguidor.", "danger")
        return _volver_a_usuarios()

    try:
        usuario_id = int(usuario_id_texto)
        seguidor_id = int(seguidor_id_texto)
    except ValueError:
        flash("Los identificadores no son válidos.", "danger")
        return _volver_a_usuarios()

    if usuario_id <= 0 or seguidor_id <= 0:
        flash("Los identificadores no son válidos.", "danger")
        return _volver_a_usuarios()

    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        flash("El usuario seleccionado no existe.", "danger")
        return _volver_a_usuarios()

    seguidor = Usuario.get_by_id(seguidor_id)
    if seguidor is None:
        flash("El seguidor seleccionado no existe.", "danger")
        return _volver_a_usuarios()

    data = {"usuario_id": usuario_id, "seguidor_id": seguidor_id}
    relacion_existente = Seguidor.existe(data)

    if relacion_existente is None:
        flash("No fue posible verificar la relación. Revisa MySQL.", "danger")
        return _volver_a_usuarios()

    if relacion_existente:
        flash("Esta relación ya existe.", "warning")
        return _volver_a_usuarios()

    resultado = Seguidor.seguir(data)

    if resultado is False:
        flash("No fue posible registrar la relación.", "danger")
        return _volver_a_usuarios()

    flash("Relación registrada correctamente.", "success")
    return _volver_a_usuarios()
