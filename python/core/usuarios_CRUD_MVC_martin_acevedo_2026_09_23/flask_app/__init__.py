from flask import Flask

# Punto central para configurar e importar la aplicación Flask.
app = Flask(__name__)

# Clave de desarrollo; reemplazar por una variable de entorno en producción.
app.secret_key = "clave-secreta-desarrollo"
