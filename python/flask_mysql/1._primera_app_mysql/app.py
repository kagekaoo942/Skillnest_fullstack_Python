# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================


from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """

    # ------------------------------------------------------
    # Consultar base de datos mediante el modelo.
    # ------------------------------------------------------

    mascotas = Mascota.get_all()


    # ------------------------------------------------------
    # Mostrar resultados en la terminal.
    # ------------------------------------------------------

    print(mascotas)


    # ------------------------------------------------------
    # Enviar resultados a Jinja2.
    # ------------------------------------------------------

    return render_template(
        "index.html",
        mascotas=mascotas
    )


@app.route("/mascota/<int:id_mascota>")
def mostrar_mascota(id_mascota):
    mascota = Mascota.get_by_id(id_mascota)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template("mascota.html", mascota=mascota)


@app.route("/mascota/nombre/<string:nombre>")
def mostrar_mascota_por_nombre(nombre):
    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template("mascota.html", mascota=mascota)


@app.route("/mascotas/tipo/<string:tipo>")
def mostrar_mascotas_por_tipo(tipo):
    mascotas = Mascota.get_by_tipo(tipo)
    return render_template("index.html", mascotas=mascotas)


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
