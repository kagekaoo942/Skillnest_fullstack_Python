from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


def _mostrar_formulario(cursos, status=200):
    """Vuelve a mostrar el formulario conservando los valores escritos."""
    form_data = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "edad": request.form.get("edad", "").strip(),
        "curso_id": request.form.get("curso_id", "").strip(),
    }
    return render_template(
        "nuevo_estudiante.html",
        cursos=cursos,
        form_data=form_data,
    ), status


@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    """Carga los cursos disponibles para el selector del formulario."""
    cursos = Curso.get_all()
    if cursos is False:
        flash(
            "No fue posible cargar los cursos. Revisa la configuración local de MySQL.",
            "danger",
        )
        cursos = []

    return render_template("nuevo_estudiante.html", cursos=cursos, form_data={})


@app.route("/estudiantes/crear", methods=["POST"])
def crear_estudiante():
    """Valida los campos y crea un estudiante relacionado con un curso."""
    cursos = Curso.get_all()
    if cursos is False:
        flash(
            "No fue posible conectar con la base de datos. "
            "Revisa la configuración local de MySQL.",
            "danger",
        )
        return redirect(url_for("nuevo_estudiante"))

    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad_texto = request.form.get("edad", "").strip()
    curso_texto = request.form.get("curso_id", "").strip()

    if not nombre or not apellido or not edad_texto or not curso_texto:
        flash("Completa todos los campos.", "warning")
        return _mostrar_formulario(cursos, 400)
    if len(nombre) > 45 or len(apellido) > 45:
        flash("El nombre y el apellido admiten hasta 45 caracteres.", "warning")
        return _mostrar_formulario(cursos, 400)

    try:
        edad = int(edad_texto)
        curso_id = int(curso_texto)
    except ValueError:
        flash("La edad y el curso deben ser valores numéricos válidos.", "warning")
        return _mostrar_formulario(cursos, 400)

    if edad < 1:
        flash("La edad debe ser un número mayor que cero.", "warning")
        return _mostrar_formulario(cursos, 400)

    curso_existe = Curso.exists(curso_id)
    if curso_existe is False:
        flash("No fue posible verificar el curso en la base de datos.", "danger")
        return _mostrar_formulario(cursos, 500)
    if not curso_existe:
        flash("Selecciona un curso válido.", "warning")
        return _mostrar_formulario(cursos, 400)

    resultado = Estudiante.save({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso_id": curso_id,
    })
    if resultado is False:
        flash("No fue posible registrar al estudiante.", "danger")
        return _mostrar_formulario(cursos, 500)

    flash("Estudiante creado.", "success")
    return redirect(url_for("cursos"))
