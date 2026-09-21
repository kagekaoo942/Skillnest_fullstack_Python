from flask import Flask, render_template, request, redirect, url_for

from usuario import Usuario


app = Flask(__name__)


@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)


@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()

    if not nombre or not apellido or not email:
        return render_template(
            "usuario_nuevo.html",
            error="Todos los campos son obligatorios.",
            datos=request.form,
        ), 400

    resultado = Usuario.save({
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
    })

    if resultado is False:
        return render_template(
            "usuario_nuevo.html",
            error="No fue posible crear el usuario.",
            datos=request.form,
        ), 500

    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)
