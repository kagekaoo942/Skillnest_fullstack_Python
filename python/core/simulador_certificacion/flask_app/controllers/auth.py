from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_user, logout_user

from flask_app import bcrypt
from flask_app.models.usuario import Usuario

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET"])
def index():
    """La entrada contiene ambos formularios como indica el wireframe."""
    if current_user.is_authenticated:
        return redirect(url_for("libros.mis_libros"))
    return render_template("auth/index.html", form_data={})


@auth.route("/registro", methods=["POST"])
def registrar():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        "password": request.form.get("password", ""),
        "confirmar_password": request.form.get("confirmar_password", ""),
    }
    errores = Usuario.validar(datos)
    if errores:
        for error in errores:
            flash(error, "danger")
        return render_template(
            "auth/index.html",
            form_data={key: value for key, value in datos.items() if key not in {"password", "confirmar_password"}},
        ), 400

    # El modelo distingue una consulta fallida, un correo inexistente y uno ya registrado.
    existente = Usuario.buscar_por_email(datos["email"])
    if existente is False:
        flash("No fue posible conectar con la base de datos. Revisa la configuración local.", "danger")
        return redirect(url_for("auth.index"))
    if existente is not None:
        flash("El correo electrónico ya está registrado.", "danger")
        return redirect(url_for("auth.index"))

    # Solo se persiste el hash; la contraseña original no se guarda en la base de datos.
    password_hash = bcrypt.generate_password_hash(datos["password"]).decode("utf-8")
    usuario_id = Usuario.crear({
        "nombre": datos["nombre"],
        "apellido": datos["apellido"],
        "email": datos["email"],
        "password_hash": password_hash,
    })
    if not usuario_id:
        flash("No fue posible crear la cuenta. Revisa los datos e inténtalo otra vez.", "danger")
        return redirect(url_for("auth.index"))

    usuario = Usuario.buscar_por_id(usuario_id)
    if usuario is None:
        flash("La cuenta se creó, pero no fue posible iniciar sesión.", "warning")
        return redirect(url_for("auth.index"))

    session.clear()
    login_user(usuario)
    flash("Cuenta creada.", "success")
    return redirect(url_for("libros.mis_libros"))


@auth.route("/login", methods=["POST"])
def iniciar_sesion():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = Usuario.buscar_por_email(email) if email else None

    if usuario is False:
        flash("No fue posible conectar con la base de datos. Inténtalo de nuevo.", "danger")
        return redirect(url_for("auth.index"))
    if usuario is None or not bcrypt.check_password_hash(usuario.password_hash, password):
        session.clear()
        flash("Correo electrónico o contraseña incorrectos.", "danger")
        return redirect(url_for("auth.index"))

    session.clear()
    login_user(usuario)
    return redirect(url_for("libros.mis_libros"))


@auth.route("/logout", methods=["POST"])
def cerrar_sesion():
    logout_user()
    session.clear()
    return redirect(url_for("auth.index"))
