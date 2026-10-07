import re
from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from flask_app.models.usuario import Usuario


auth_bp = Blueprint("auth", __name__)
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def login_required(view):
    @wraps(view)
    def protected(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesión.", "error")
            return redirect(url_for("auth.inicio"))
        return view(*args, **kwargs)

    return protected


@auth_bp.get("/")
def inicio():
    return render_template("inicio.html")


@auth_bp.post("/registro")
def registro():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    if len(nombre) < 2 or len(apellido) < 2:
        flash("Nombre y apellido deben tener al menos 2 caracteres.", "error")
        return redirect(url_for("auth.inicio"))
    if not EMAIL_RE.fullmatch(email):
        flash("Ingresa un correo electrónico válido.", "error")
        return redirect(url_for("auth.inicio"))
    if len(password) < 2 or password != confirm_password:
        flash("La contraseña debe tener al menos 2 caracteres y coincidir.", "error")
        return redirect(url_for("auth.inicio"))
    if Usuario.buscar_por_email(email):
        flash("El correo ya está registrado.", "error")
        return redirect(url_for("auth.inicio"))

    usuario_id = Usuario.crear(
        {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "password": generate_password_hash(password),
        }
    )
    session.clear()
    session["usuario_id"] = usuario_id
    session["usuario_nombre"] = nombre
    return redirect(url_for("tareas.dashboard"))


@auth_bp.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = Usuario.buscar_por_email(email)

    if usuario is None or not check_password_hash(usuario["password"], password):
        flash("Correo o contraseña incorrectos.", "error")
        return redirect(url_for("auth.inicio"))

    session.clear()
    session["usuario_id"] = usuario["id"]
    session["usuario_nombre"] = usuario["nombre"]
    return redirect(url_for("tareas.dashboard"))


@auth_bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.inicio"))


@auth_bp.get("/perfil")
@login_required
def perfil():
    usuario = Usuario.buscar_por_id(session["usuario_id"])
    if usuario is None:
        session.clear()
        flash("Tu sesión ya no es válida.", "error")
        return redirect(url_for("auth.inicio"))
    return render_template("perfil.html", usuario=usuario)
