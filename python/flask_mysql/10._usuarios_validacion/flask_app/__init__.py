import os

from flask import Flask

app = Flask(__name__)

# La clave se puede sobrescribir con una variable de entorno en despliegues.
app.secret_key = os.getenv("FLASK_SECRET_KEY", "clave-secreta-desarrollo")
