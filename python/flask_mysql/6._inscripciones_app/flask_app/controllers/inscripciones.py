from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante
from flask_app.models.inscripcion import Inscripcion


@app.route("/")
def index():
    """Carga entidades y relaciones para el formulario principal."""
    estudiantes = Estudiante.get_all() or []
    cursos = Curso.get_all() or []
    inscripciones = Inscripcion.get_all() or []

    return render_template(
        "index.html",
        estudiantes=estudiantes,
        cursos=cursos,
        inscripciones=inscripciones
    )


@app.route("/inscribir", methods=["POST"])
def inscribir():
    """Valida los IDs, evita duplicados y crea una inscripción."""
    estudiante_id_texto = request.form.get("estudiante_id", "").strip()
    curso_id_texto = request.form.get("curso_id", "").strip()

    if not estudiante_id_texto or not curso_id_texto:
        flash("Debes seleccionar un estudiante y un curso.", "danger")
        return redirect(url_for("index"))

    try:
        estudiante_id = int(estudiante_id_texto)
        curso_id = int(curso_id_texto)
        if estudiante_id <= 0 or curso_id <= 0:
            raise ValueError
    except ValueError:
        flash("Los identificadores no son válidos.", "danger")
        return redirect(url_for("index"))

    estudiante = Estudiante.get_by_id(estudiante_id)
    if estudiante is None:
        flash("El estudiante seleccionado no existe.", "danger")
        return redirect(url_for("index"))

    curso = Curso.get_by_id(curso_id)
    if curso is None:
        flash("El curso seleccionado no existe.", "danger")
        return redirect(url_for("index"))

    data = {
        "estudiante_id": estudiante_id,
        "curso_id": curso_id
    }

    if Inscripcion.existe(data):
        flash("El estudiante ya está inscrito en este curso.", "warning")
        return redirect(url_for("index"))

    resultado = Inscripcion.inscribir_estudiante_en_curso(data)
    if resultado is False:
        flash("No fue posible crear la inscripción.", "danger")
        return redirect(url_for("index"))

    flash("Inscripción realizada correctamente.", "success")
    return redirect(url_for("index"))
