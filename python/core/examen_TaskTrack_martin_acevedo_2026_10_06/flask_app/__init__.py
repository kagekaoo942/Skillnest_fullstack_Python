import os

from flask import Flask

from flask_app.controllers.auth import auth_bp
from flask_app.controllers.categorias import categorias_bp
from flask_app.controllers.tareas import tareas_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        static_url_path="/static",
    )
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

    app.register_blueprint(auth_bp)
    app.register_blueprint(tareas_bp)
    app.register_blueprint(categorias_bp)
    return app
