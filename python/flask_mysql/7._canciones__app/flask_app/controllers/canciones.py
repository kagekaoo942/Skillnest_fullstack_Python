from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    """Envía la raíz de la aplicación al listado de usuarios."""
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    """Muestra todos los usuarios y el formulario de alta."""
    return render_template("usuarios.html", usuarios=Usuario.get_all())


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    """Valida y guarda un usuario nuevo."""
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "email": request.form.get("email", "").strip(),
        "contrasena": request.form.get("contrasena", "").strip(),
    }

    if not all(data.values()):
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("usuarios"))

    if any(len(data[campo]) > 45 for campo in data):
        flash("Cada campo debe tener como máximo 45 caracteres.", "danger")
        return redirect(url_for("usuarios"))

    resultado = Usuario.save(data)
    if resultado is False:
        flash("No fue posible crear el usuario.", "danger")
    else:
        flash("Usuario creado correctamente.", "success")

    return redirect(url_for("usuarios"))


@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    """Muestra un usuario, sus favoritos y el formulario para agregar."""
    usuario = Usuario.get_by_id_with_favorites({"id": id})
    if usuario is None:
        return "Usuario no encontrado", 404

    return render_template(
        "mostrar_usuario.html",
        usuario=usuario,
        canciones=Cancion.get_all(),
    )


@app.route("/canciones")
def canciones():
    """Muestra las canciones y el formulario de alta."""
    return render_template("canciones.html", canciones=Cancion.get_all())


@app.route("/canciones/crear", methods=["POST"])
def crear_cancion():
    """Valida y guarda una canción nueva."""
    data = {
        "titulo": request.form.get("titulo", "").strip(),
        "artista": request.form.get("artista", "").strip(),
    }

    if not all(data.values()):
        flash("Título y artista son obligatorios.", "danger")
        return redirect(url_for("canciones"))

    if any(len(valor) > 45 for valor in data.values()):
        flash("Título y artista deben tener como máximo 45 caracteres.", "danger")
        return redirect(url_for("canciones"))

    resultado = Cancion.save(data)
    if resultado is False:
        flash("No fue posible crear la canción.", "danger")
    else:
        flash("Canción creada correctamente.", "success")

    return redirect(url_for("canciones"))


@app.route("/canciones/<int:id>")
def mostrar_cancion(id):
    """Muestra la canción y usuarios aún disponibles para favoritarla."""
    data = {"id": id}
    cancion = Cancion.get_by_id_with_users(data)
    if cancion is None:
        return "Canción no encontrada", 404

    usuarios_disponibles = Cancion.get_users_not_favorited({"cancion_id": id})
    return render_template(
        "mostrar_cancion.html",
        cancion=cancion,
        usuarios=usuarios_disponibles,
    )


@app.route("/favoritos/agregar", methods=["POST"])
def agregar_favorito():
    """Valida la pareja de IDs, evita duplicados y guarda el favorito."""
    usuario_id_texto = request.form.get("usuario_id", "").strip()
    cancion_id_texto = request.form.get("cancion_id", "").strip()
    origen = request.form.get("origen", "")

    if not usuario_id_texto or not cancion_id_texto:
        flash("Debes seleccionar los datos necesarios.", "danger")
        return redirect(url_for("usuarios"))

    try:
        usuario_id = int(usuario_id_texto)
        cancion_id = int(cancion_id_texto)
        if usuario_id <= 0 or cancion_id <= 0:
            raise ValueError
    except ValueError:
        flash("Los identificadores no son válidos.", "danger")
        return redirect(url_for("usuarios"))

    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        flash("El usuario seleccionado no existe.", "danger")
        return redirect(url_for("usuarios"))

    cancion = Cancion.get_by_id(cancion_id)
    if cancion is None:
        flash("La canción seleccionada no existe.", "danger")
        return redirect(url_for("canciones"))

    data = {"usuario_id": usuario_id, "cancion_id": cancion_id}
    if Favorito.existe(data):
        flash("Esta canción ya está entre los favoritos del usuario.", "warning")
    else:
        resultado = Favorito.agregar(data)
        if resultado is False:
            flash("No fue posible agregar el favorito.", "danger")
        else:
            flash("Favorito agregado correctamente.", "success")

    if origen == "usuario":
        return redirect(url_for("mostrar_usuario", id=usuario_id))
    if origen == "cancion":
        return redirect(url_for("mostrar_cancion", id=cancion_id))
    return redirect(url_for("usuarios"))
