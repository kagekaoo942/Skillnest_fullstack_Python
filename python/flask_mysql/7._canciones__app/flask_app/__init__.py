from flask import Flask

app = Flask(__name__)

# Clave de desarrollo necesaria para los mensajes flash.
app.secret_key = "clave-secreta-desarrollo"
