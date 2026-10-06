import os
import re
from functools import wraps

import pymysql
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY", "dev-key-change-me"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "false").lower() == "true",
)

NAME_PATTERN = re.compile(r"^[^\W\d_]+$", re.UNICODE)
EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "inicio_sesion"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def query_one(query, params):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()
    finally:
        connection.close()


def insert_user(user_data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuarios (nombre, apellido, email, password)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)
                """,
                user_data,
            )
            return cursor.lastrowid
    finally:
        connection.close()


def validate_registration(form):
    errors = []
    nombre = form.get("nombre", "").strip()
    apellido = form.get("apellido", "").strip()
    email = form.get("email", "").strip().lower()
    password = form.get("password", "")
    confirm_password = form.get("confirm_password", "")

    if not nombre:
        errors.append("El nombre es obligatorio.")
    elif len(nombre) < 2 or not NAME_PATTERN.fullmatch(nombre):
        errors.append("El nombre debe tener al menos 2 caracteres y solo letras.")

    if not apellido:
        errors.append("El apellido es obligatorio.")
    elif len(apellido) < 2 or not NAME_PATTERN.fullmatch(apellido):
        errors.append("El apellido debe tener al menos 2 caracteres y solo letras.")

    if not email:
        errors.append("El correo electrónico es obligatorio.")
    elif not EMAIL_PATTERN.fullmatch(email):
        errors.append("El correo electrónico no tiene un formato válido.")

    if not password:
        errors.append("La contraseña es obligatoria.")
    elif len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres.")
    else:
        if not re.search(r"[A-Z]", password):
            errors.append("La contraseña debe incluir al menos una mayúscula.")
        if not re.search(r"\d", password):
            errors.append("La contraseña debe incluir al menos un número.")

    if password != confirm_password:
        errors.append("La confirmación de contraseña no coincide.")

    return errors, {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password,
    }


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesión para ver esta página.", "error")
            return redirect(url_for("index"))
        return view(*args, **kwargs)

    return wrapped_view


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/registrar")
def register():
    errors, user_data = validate_registration(request.form)
    if errors:
        for error in errors:
            flash(error, "error")
        return redirect(url_for("index"))

    try:
        if query_one("SELECT id FROM usuarios WHERE email = %(email)s", user_data):
            flash("Este correo electrónico ya está registrado.", "error")
            return redirect(url_for("index"))

        user_data["password"] = generate_password_hash(user_data["password"])
        user_id = insert_user(user_data)
    except pymysql.err.IntegrityError:
        flash("Este correo electrónico ya está registrado.", "error")
        return redirect(url_for("index"))
    except pymysql.MySQLError:
        flash("No fue posible conectar con la base de datos.", "error")
        return redirect(url_for("index"))

    session.clear()
    session["usuario_id"] = user_id
    flash("¡Registro exitoso! Bienvenido.", "success")
    return redirect(url_for("success"))


@app.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    try:
        user = query_one(
            "SELECT id, nombre, password FROM usuarios WHERE email = %(email)s",
            {"email": email},
        )
    except pymysql.MySQLError:
        flash("No fue posible conectar con la base de datos.", "error")
        return redirect(url_for("index"))

    if not email or not password or user is None or not check_password_hash(
        user["password"], password
    ):
        flash("El correo electrónico o la contraseña son incorrectos.", "error")
        return redirect(url_for("index"))

    session.clear()
    session["usuario_id"] = user["id"]
    return redirect(url_for("success"))


@app.get("/success")
@login_required
def success():
    try:
        user = query_one(
            "SELECT id, nombre, apellido, email FROM usuarios WHERE id = %(id)s",
            {"id": session["usuario_id"]},
        )
    except pymysql.MySQLError:
        session.clear()
        flash("No fue posible consultar tu usuario.", "error")
        return redirect(url_for("index"))

    if user is None:
        session.clear()
        flash("Tu sesión ya no es válida.", "error")
        return redirect(url_for("index"))
    return render_template("success.html", user=user)


@app.get("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
