from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.curso import Curso


@app.route("/")
def inicio():
    """Envía la página raíz al listado de cursos."""
    return redirect(url_for("cursos"))


@app.route("/cursos")
def cursos():
    """Muestra el formulario y el listado de cursos."""
    todos_los_cursos = Curso.get_all()
    if todos_los_cursos is False:
        flash(
            "No fue posible conectar con la base de datos. "
            "Revisa la configuración local de MySQL.",
            "danger",
        )
        todos_los_cursos = []

    return render_template("cursos.html", cursos=todos_los_cursos)


@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    """Valida y guarda el nombre recibido desde el formulario."""
    nombre = request.form.get("nombre", "").strip()
    if not nombre:
        flash("Escribe el nombre del curso.", "warning")
        return redirect(url_for("cursos"))
    if len(nombre) > 45:
        flash("El nombre del curso no puede superar 45 caracteres.", "warning")
        return redirect(url_for("cursos"))

    resultado = Curso.save({"nombre": nombre})
    if resultado is False:
        flash("No fue posible guardar el curso.", "danger")
        return redirect(url_for("cursos"))

    flash("Curso creado.", "success")
    return redirect(url_for("cursos"))


@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    """Muestra un curso con la lista de estudiantes relacionados."""
    curso = Curso.get_curso_con_estudiantes(id)
    if curso is False:
        flash(
            "No fue posible consultar la base de datos. "
            "Revisa la configuración local de MySQL.",
            "danger",
        )
        return redirect(url_for("cursos"))
    if curso is None:
        flash("El curso solicitado no existe.", "warning")
        return redirect(url_for("cursos"))

    return render_template("mostrar_curso.html", curso=curso)
