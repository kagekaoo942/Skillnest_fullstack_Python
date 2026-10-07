from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from flask_app.controllers.auth import login_required
from flask_app.models.categoria import Categoria


categorias_bp = Blueprint("categorias", __name__)


@categorias_bp.get("/categorias")
@login_required
def listar():
    return render_template("categorias.html", categorias=Categoria.listar_con_tareas(session["usuario_id"]))


@categorias_bp.get("/categorias/nueva")
@login_required
def nueva():
    return render_template("categoria_nueva.html")


@categorias_bp.post("/categorias/crear")
@login_required
def crear():
    nombre = request.form.get("nombre", "").strip()
    if not nombre:
        flash("El nombre de la categoría es obligatorio.", "error")
    else:
        Categoria.crear(nombre, session["usuario_id"])
    return redirect(url_for("categorias.listar"))


@categorias_bp.get("/categorias/<int:categoria_id>")
@login_required
def detalle(categoria_id):
    categoria = Categoria.buscar(categoria_id, session["usuario_id"])
    if categoria is None:
        flash("La categoría no existe.", "error")
        return redirect(url_for("categorias.listar"))
    return render_template("categoria_detalle.html", categoria=categoria)


@categorias_bp.get("/categorias/editar/<int:categoria_id>")
@login_required
def editar(categoria_id):
    categoria = Categoria.buscar(categoria_id, session["usuario_id"])
    if categoria is None:
        flash("La categoría no existe.", "error")
        return redirect(url_for("categorias.listar"))
    return render_template("categoria_editar.html", categoria=categoria)


@categorias_bp.post("/categorias/actualizar/<int:categoria_id>")
@login_required
def actualizar(categoria_id):
    nombre = request.form.get("nombre", "").strip()
    if not nombre:
        flash("El nombre de la categoría es obligatorio.", "error")
        return redirect(url_for("categorias.editar", categoria_id=categoria_id))
    Categoria.actualizar(categoria_id, session["usuario_id"], nombre)
    return redirect(url_for("categorias.listar"))


@categorias_bp.get("/categorias/borrar/<int:categoria_id>")
@login_required
def borrar(categoria_id):
    Categoria.eliminar(categoria_id, session["usuario_id"])
    return redirect(url_for("categorias.listar"))
