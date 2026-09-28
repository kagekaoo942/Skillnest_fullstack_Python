from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario


@app.route("/")
def index():
    """Presenta el formulario de inicio de sesión."""
    return render_template("login.html")


@app.route("/registro")
def registro():
    """Muestra el formulario para crear una cuenta."""
    return render_template("registro.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    """Valida la cuenta y guarda únicamente un hash de la contraseña."""
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        # La contraseña no se elimina del contenido, transforma ni guarda en sesión.
        "password": request.form.get("password", ""),
    }

    if not Usuario.validar_usuario(datos):
        return redirect(url_for("registro"))

    email_ya_registrado = Usuario.existe_email({"email": datos["email"]})
    if email_ya_registrado is None:
        flash(
            "No fue posible conectar con la base de datos. "
            "Revisa DB_HOST, DB_USER, DB_PASSWORD y DB_NAME.",
            "general",
        )
        return redirect(url_for("registro"))

    if email_ya_registrado:
        flash("El email ya está registrado.", "email")
        return redirect(url_for("registro"))

    datos_para_guardar = {
        **datos,
        "password": bcrypt.generate_password_hash(datos["password"]).decode("utf-8"),
    }
    usuario_id = Usuario.guardar(datos_para_guardar)

    # El índice UNIQUE también cubre la colisión entre la comprobación y el INSERT.
    if not usuario_id:
        flash("No fue posible registrar el usuario.", "general")
        return redirect(url_for("registro"))

    session.clear()
    session["usuario_id"] = usuario_id
    flash("Usuario creado.", "success")
    return redirect(url_for("dashboard"))


@app.route("/login", methods=["POST"])
def login():
    """Autentica una cuenta con el hash almacenado y un mensaje genérico."""
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        session.clear()
        flash("Email o contraseña incorrectos.", "login")
        return redirect(url_for("index"))

    usuario = Usuario.buscar_por_email({"email": email})
    if usuario is None or not bcrypt.check_password_hash(usuario.password, password):
        session.clear()
        flash("Email o contraseña incorrectos.", "login")
        return redirect(url_for("index"))

    session.clear()
    session["usuario_id"] = usuario.id
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    """Protege el dashboard y carga el usuario de la sesión actual."""
    usuario_id = session.get("usuario_id")
    if usuario_id is None:
        flash("Debes iniciar sesión.", "login")
        return redirect(url_for("index"))

    usuario = Usuario.buscar_por_id({"id": usuario_id})
    if usuario is None:
        # Una sesión con un usuario eliminado ya no representa una cuenta válida.
        session.clear()
        flash("Debes iniciar sesión.", "login")
        return redirect(url_for("index"))

    return render_template("dashboard.html", usuario=usuario)


@app.route("/logout")
def logout():
    """Cierra la sesión eliminando sus datos y regresa al login."""
    session.clear()
    return redirect(url_for("index"))
