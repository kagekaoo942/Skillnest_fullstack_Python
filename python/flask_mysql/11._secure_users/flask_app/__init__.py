import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt

# Carga explícita desde la raíz de este proyecto antes de crear extensiones.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
if not secret_key:
    raise RuntimeError(
        "Falta SECRET_KEY. Configúrala en el archivo .env antes de iniciar Flask."
    )

app.config.update(
    SECRET_KEY=secret_key,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "false").lower() == "true",
)

bcrypt = Bcrypt(app)

# La importación registra las rutas después de inicializar app y bcrypt.
from flask_app.controllers import usuarios  # noqa: E402,F401
