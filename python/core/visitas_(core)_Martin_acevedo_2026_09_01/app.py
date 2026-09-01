# ==========================================================
# VISITAS - SESIONES EN FLASK
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)


# ==========================================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# SECRET KEY
# ==========================================================
#
# Flask necesita una clave secreta para utilizar session.
#
# Esta clave permite firmar y proteger la información
# asociada a la sesión.
#
# En una aplicación real no deberíamos dejar una clave
# sensible escrita directamente en el código fuente.
#
# Para esta actividad utilizamos una clave únicamente
# con fines educativos.
# ==========================================================

app.secret_key = "clave-secreta-visitas"


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra la cantidad de visitas del usuario.

    Cada vez que se accede a esta ruta se considera
    una nueva visita.
    """

    # ------------------------------------------------------
    # COMPROBAR SI EXISTE EL CONTADOR
    # ------------------------------------------------------

    if "visitas" in session:

        # Si ya existe, aumentamos una visita.

        session["visitas"] += 1

    else:

        # Si no existe, inicializamos el contador.

        session["visitas"] = 1


    # ------------------------------------------------------
    # INICIALIZAR CONTADOR DE REINICIOS
    # ------------------------------------------------------

    if "reinicios" not in session:

        session["reinicios"] = 0


    # ------------------------------------------------------
    # ENVIAR INFORMACIÓN A LA PLANTILLA
    # ------------------------------------------------------

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


# ==========================================================
# AUMENTAR VISITAS EN 2
# ==========================================================

@app.route("/sumar_dos")
def sumar_dos():
    """
    Aumenta el contador de visitas en dos unidades.
    """

    # Si no existe el contador, lo inicializamos.

    if "visitas" not in session:

        session["visitas"] = 0


    # Aumentamos la cantidad en dos.

    session["visitas"] += 2


    # Volvemos a la página principal.

    return redirect(url_for("index"))


# ==========================================================
# REINICIAR CONTADOR
# ==========================================================

@app.route("/reiniciar")
def reiniciar():
    """
    Reinicia el contador de visitas.

    Además registra que se realizó un reinicio.
    """

    # ------------------------------------------------------
    # ASEGURAR QUE EXISTA EL CONTADOR DE REINICIOS
    # ------------------------------------------------------

    if "reinicios" not in session:

        session["reinicios"] = 0


    # Registrar un nuevo reinicio.

    session["reinicios"] += 1


    # Reiniciar contador de visitas.

    session["visitas"] = 0


    # Volver a la página principal.

    return redirect(url_for("index"))


# ==========================================================
# SUMAR UNA CANTIDAD PERSONALIZADA
# ==========================================================

@app.route("/sumar", methods=["POST"])
def sumar():
    """
    Recibe una cantidad desde un formulario
    y la agrega al contador de visitas.
    """

    # ------------------------------------------------------
    # OBTENER INFORMACIÓN DEL FORMULARIO
    # ------------------------------------------------------

    cantidad = int(
        request.form["cantidad"]
    )


    # ------------------------------------------------------
    # COMPROBAR QUE EXISTA EL CONTADOR
    # ------------------------------------------------------

    if "visitas" not in session:

        session["visitas"] = 0


    # ------------------------------------------------------
    # SUMAR CANTIDAD
    # ------------------------------------------------------

    session["visitas"] += cantidad


    # ------------------------------------------------------
    # REDIRECCIONAR
    # ------------------------------------------------------

    return redirect(url_for("index"))


# ==========================================================
# DESTRUIR TODA LA SESIÓN
# ==========================================================

@app.route("/destruir_sesion")
def destruir_sesion():
    """
    Elimina todas las propiedades almacenadas
    en la sesión del usuario.
    """

    # Elimina completamente el contenido de session.

    session.clear()


    # Volvemos al inicio.

    return redirect(url_for("index"))


# ==========================================================
# EJECUTAR APLICACIÓN
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
