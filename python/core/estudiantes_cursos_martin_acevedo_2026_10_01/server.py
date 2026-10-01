from flask_app import app

# Las importaciones registran las rutas en la aplicación Flask.
from flask_app.controllers import cursos, estudiantes  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
