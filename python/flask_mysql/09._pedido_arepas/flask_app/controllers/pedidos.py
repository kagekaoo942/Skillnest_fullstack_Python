from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.pedido import Pedido


@app.route("/")
def inicio():
    """La ruta raíz redirige al listado de pedidos."""
    return redirect(url_for("pedidos"))


@app.route("/arepas")
@app.route("/pedidos")
def pedidos():
    """Carga desde MySQL y muestra todos los pedidos."""
    return render_template("pedidos.html", pedidos=Pedido.get_all())


@app.route("/pedido")
@app.route("/pedidos/nuevo")
def nuevo_pedido():
    """Muestra el formulario de creación de pedidos."""
    return render_template("nuevo_pedido.html")


@app.route("/pedidos/crear", methods=["POST"])
def crear_pedido():
    """Valida los datos del formulario y guarda pedidos válidos."""
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "tipo_arepa": request.form.get("tipo_arepa", "").strip(),
        "cantidad": request.form.get("cantidad", "").strip(),
    }

    # No se intenta guardar hasta que todas las reglas se cumplan.
    if not Pedido.validar_pedido(data):
        return redirect(url_for("nuevo_pedido"))

    data["cantidad"] = int(data["cantidad"])
    resultado = Pedido.save(data)

    if resultado is False:
        flash("No fue posible guardar el pedido.", "danger")
        return redirect(url_for("nuevo_pedido"))

    flash("Pedido creado correctamente.", "success")
    return redirect(url_for("pedidos"))
