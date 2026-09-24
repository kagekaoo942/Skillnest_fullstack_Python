from flask_app import app

# La importación registra las rutas definidas en el controlador.
from flask_app.controllers import tacos


if __name__ == "__main__":
    app.run(debug=True)
