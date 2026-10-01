import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

# Cargar la configuración local antes de inicializar la aplicación.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "clave-de-desarrollo-cambiar-en-produccion",
)
