import os
from pathlib import Path
import secrets

from dotenv import load_dotenv
from flask import Flask, abort, request, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Carga la configuración desde esta aplicación, aunque Flask se inicie desde otra carpeta.
load_dotenv(PROJECT_ROOT / ".env")

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
# Se detiene el arranque si las sesiones no pueden firmarse de forma segura.
if not secret_key:
    raise RuntimeError("Configura SECRET_KEY en el archivo .env antes de iniciar BookHub.")

app.config.update(
    SECRET_KEY=secret_key,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "false").lower() == "true",
    REMEMBER_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_SAMESITE="Lax",
)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.index"
login_manager.login_message = "Debes iniciar sesión para continuar."
login_manager.login_message_category = "warning"


@app.before_request
def protect_post_requests():
    """Añade un token CSRF a la sesión y valida cada formulario POST."""
    if "_csrf_token" not in session:
        session["_csrf_token"] = secrets.token_urlsafe(32)

    if request.method == "POST":
        import hmac

        submitted_token = request.form.get("csrf_token", "")
        session_token = session.get("_csrf_token", "")
        # La comparación de tiempo constante reduce filtraciones sobre el token esperado.
        if not submitted_token or not hmac.compare_digest(submitted_token, session_token):
            abort(400, description="El formulario expiró. Recarga la página e inténtalo otra vez.")


@app.context_processor
def inject_csrf_token():
    return {"csrf_token": lambda: session.get("_csrf_token", "")}


@login_manager.user_loader
def load_user(user_id):
    from flask_app.models.usuario import Usuario

    try:
        return Usuario.buscar_por_id(int(user_id))
    except (TypeError, ValueError):
        return None


# Las importaciones registran las rutas tras inicializar Flask y sus extensiones.
from flask_app.controllers import auth, libros  # noqa: E402,F401
