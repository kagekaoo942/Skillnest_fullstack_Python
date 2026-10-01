from flask_app import app
from flask_app.controllers.auth import auth
from flask_app.controllers.libros import libros

app.register_blueprint(auth)
app.register_blueprint(libros)
