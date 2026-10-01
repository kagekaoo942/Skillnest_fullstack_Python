from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from flask_app.models.favorito import Favorito
from flask_app.models.libro import (
    FECHA_PUBLICACION_MAXIMA,
    FECHA_PUBLICACION_MINIMA,
    GENEROS_LIBRO,
    Libro,
)

libros = Blueprint("libros", __name__)


def _form_data():
    return {
        "titulo": request.form.get("titulo", "").strip(),
        "autor": request.form.get("autor", "").strip(),
        "genero": request.form.get("genero", "").strip(),
        "fecha_publicacion": request.form.get("fecha_publicacion", "").strip(),
        "descripcion": request.form.get("descripcion", "").strip(),
    }


def _buscar_propietario(libro_id):
    # La consulta verifica a la vez que el libro exista y pertenezca al usuario actual.
    libro = Libro.obtener_propietario(libro_id, current_user.id)
    if libro is False:
        abort(503, description="No fue posible consultar la biblioteca.")
    if libro is None:
        abort(404)
    return libro


def _guardar_formulario(libro, datos, modo, status=200):
    return render_template(
        "libros/formulario.html",
        libro=libro,
        form_data=datos,
        modo=modo,
        generos=GENEROS_LIBRO,
        fecha_minima=FECHA_PUBLICACION_MINIMA.isoformat(),
        fecha_maxima=FECHA_PUBLICACION_MAXIMA.isoformat(),
    ), status


@libros.route("/libros")
@login_required
def mis_libros():
    propios = Libro.obtener_todos_del_usuario(current_user.id)
    comunidad = Libro.obtener_comunidad(current_user.id)
    if propios is False or comunidad is False:
        flash("No fue posible cargar todos los libros. Inténtalo de nuevo.", "danger")
        propios = [] if propios is False else propios
        comunidad = [] if comunidad is False else comunidad
    return render_template(
        "libros/index.html",
        libros=propios,
        libros_comunidad=comunidad,
    )


@libros.route("/libros/nuevo", methods=["GET"])
@login_required
def nuevo():
    return _guardar_formulario(None, {}, "crear")


@libros.route("/libros", methods=["POST"])
@login_required
def crear():
    datos, errores = Libro.validar(_form_data())
    if errores:
        for error in errores:
            flash(error, "danger")
        return _guardar_formulario(None, _form_data(), "crear", 400)

    resultado = Libro.crear(current_user.id, datos)
    if resultado is False:
        flash("No fue posible guardar el libro. Inténtalo de nuevo.", "danger")
        return _guardar_formulario(None, _form_data(), "crear", 500)

    flash("Libro añadido.", "success")
    return redirect(url_for("libros.detalle", libro_id=resultado))


@libros.route("/libros/<int:libro_id>")
@login_required
def detalle(libro_id):
    libro = Libro.obtener_visible(libro_id)
    if libro is False:
        abort(503, description="No fue posible consultar el libro.")
    if libro is None:
        abort(404)

    es_favorito = Favorito.existe(current_user.id, libro_id)
    if es_favorito is None:
        abort(503, description="No fue posible consultar tus favoritos.")
    usuarios_favoritos = Favorito.obtener_usuarios(libro_id)
    if usuarios_favoritos is False:
        usuarios_favoritos = []

    return render_template(
        "libros/detalle.html",
        libro=libro,
        es_favorito=es_favorito,
        usuarios_favoritos=usuarios_favoritos,
        es_propietario=(libro.usuario_id == current_user.id),
    )


@libros.route("/libros/editar/<int:libro_id>", methods=["GET", "POST"])
@login_required
def editar(libro_id):
    libro = _buscar_propietario(libro_id)
    if request.method == "GET":
        form_data = {
            "titulo": libro.titulo,
            "autor": libro.autor,
            "genero": libro.genero,
            "fecha_publicacion": libro.fecha_publicacion.isoformat(),
            "descripcion": libro.descripcion,
        }
        return _guardar_formulario(libro, form_data, "editar")

    datos_formulario = _form_data()
    datos, errores = Libro.validar(datos_formulario)
    if errores:
        for error in errores:
            flash(error, "danger")
        return _guardar_formulario(libro, datos_formulario, "editar", 400)

    resultado = Libro.actualizar_propietario(libro_id, current_user.id, datos)
    if resultado is False:
        flash("No fue posible actualizar el libro. Inténtalo de nuevo.", "danger")
        return _guardar_formulario(libro, datos_formulario, "editar", 500)

    flash("Libro actualizado.", "success")
    return redirect(url_for("libros.detalle", libro_id=libro_id))


@libros.route("/libros/<int:libro_id>/borrar", methods=["POST"])
@login_required
def borrar(libro_id):
    _buscar_propietario(libro_id)
    resultado = Libro.eliminar_propietario(libro_id, current_user.id)
    if resultado is False:
        flash("No fue posible borrar el libro.", "danger")
    else:
        flash("Libro borrado.", "success")
    return redirect(url_for("libros.mis_libros"))


@libros.route("/libros/<int:libro_id>/favoritos", methods=["POST"])
@login_required
def agregar_favorito(libro_id):
    libro = Libro.obtener_visible(libro_id)
    if libro is False:
        abort(503, description="No fue posible consultar el libro.")
    if libro is None:
        abort(404)

    ya_es_favorito = Favorito.existe(current_user.id, libro_id)
    if ya_es_favorito is None:
        abort(503, description="No fue posible consultar tus favoritos.")
    if not ya_es_favorito:
        # La consulta previa evita duplicados y la clave compuesta de la tabla los refuerza.
        agregado = Favorito.agregar(current_user.id, libro_id)
        if agregado is False:
            flash("No fue posible agregar el favorito.", "danger")
            return redirect(url_for("libros.detalle", libro_id=libro_id))
        flash("Libro agregado a Favoritos.", "success")
    return redirect(url_for("libros.detalle", libro_id=libro_id))


@libros.route("/libros/favoritos")
@login_required
def mis_favoritos():
    favoritos = Libro.obtener_favoritos_del_usuario(current_user.id)
    if favoritos is False:
        flash("No fue posible cargar tus favoritos.", "danger")
        favoritos = []
    return render_template("libros/favoritos.html", libros=favoritos)
