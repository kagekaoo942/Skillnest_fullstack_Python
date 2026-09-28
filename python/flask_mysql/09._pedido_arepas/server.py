from flask_app import app

# Importar el controlador registra las rutas de la aplicación.
from flask_app.controllers import pedidos


if __name__ == "__main__":
    app.run(debug=True)
