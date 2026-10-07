from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from flask_app.controllers.auth import login_required
from flask_app.models.categoria import Categoria
from flask_app.models.tarea import Tarea


tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.get("/dashboard")
@login_required
def dashboard():
    usuario_id = session["usuario_id"]
    return render_template(
        "tareas.html",
        tareas=Tarea.listar(usuario_id),
        proximas_tareas=Tarea.proximas(usuario_id),
        resumen=Tarea.resumen(usuario_id),
    )


@tareas_bp.get("/tareas/nueva")
@login_required
def nueva():
    return render_template("tarea_nueva.html", categorias=Categoria.listar(session["usuario_id"]))


@tareas_bp.post("/tareas/crear")
@login_required
def crear():
    datos = _datos_formulario()
    if not datos["titulo"] or not datos["categoria_id"] or not datos["prioridad"]:
        flash("Título, categoría y prioridad son obligatorios.", "error")
        return redirect(url_for("tareas.nueva"))
    Tarea.crear(datos)
    return redirect(url_for("tareas.dashboard"))


@tareas_bp.get("/tareas/<int:tarea_id>")
@login_required
def detalle(tarea_id):
    tarea = Tarea.buscar(tarea_id, session["usuario_id"])
    if tarea is None:
        flash("La tarea no existe.", "error")
        return redirect(url_for("tareas.dashboard"))
    return render_template("detalle.html", tarea=tarea)


@tareas_bp.get("/tareas/editar/<int:tarea_id>")
@login_required
def editar(tarea_id):
    tarea = Tarea.buscar(tarea_id, session["usuario_id"])
    if tarea is None:
        flash("La tarea no existe.", "error")
        return redirect(url_for("tareas.dashboard"))
    return render_template(
        "editar.html",
        tarea=tarea,
        categorias=Categoria.listar(session["usuario_id"]),
    )


@tareas_bp.post("/tareas/actualizar/<int:tarea_id>")
@login_required
def actualizar(tarea_id):
    datos = _datos_formulario()
    if (
        not datos["titulo"]
        or not datos["categoria_id"]
        or not datos["prioridad"]
        or Categoria.buscar(datos["categoria_id"], session["usuario_id"]) is None
    ):
        flash("Los datos de la tarea no son válidos.", "error")
        return redirect(url_for("tareas.editar", tarea_id=tarea_id))
    Tarea.actualizar(tarea_id, session["usuario_id"], datos)
    return redirect(url_for("tareas.dashboard"))


@tareas_bp.get("/tareas/borrar/<int:tarea_id>")
@login_required
def borrar(tarea_id):
    Tarea.eliminar(tarea_id, session["usuario_id"])
    return redirect(url_for("tareas.dashboard"))


def _datos_formulario():
    categoria_id = request.form.get("categoria_id", "").strip()
    return {
        "titulo": request.form.get("titulo", "").strip(),
        "categoria_id": int(categoria_id) if categoria_id.isdigit() else None,
        "prioridad": request.form.get("prioridad", "").strip(),
        "fecha_limite": request.form.get("fecha_limite") or None,
        "descripcion": request.form.get("descripcion", "").strip(),
    }
