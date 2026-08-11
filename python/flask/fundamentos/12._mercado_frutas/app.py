# ==========================================
# Importaciones
# ==========================================

from flask import Flask, render_template, request

# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)

# ==========================================
# Base de datos ficticia
# ==========================================

frutas = [
    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.png",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },
    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.png",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },
    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.png",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },
    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "fresa.png",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },
    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.png",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },
    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "pina.png",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },
    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.png",
        "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano."
    },
    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.png",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }
]

# ==========================================
# PRIMERA RUTA: Página Principal
# URL: http://127.0.0.1:5000/
# ==========================================

@app.route("/")
def index():
    """
    Primera ruta: Renderiza 'index.html', el cual contiene el formulario 
    para seleccionar frutas e ingresar la información de contacto.
    """
    return render_template(
        "index.html",
        frutas=frutas
    )

# ==========================================
# SEGUNDA RUTA: Catálogo de Frutas (Imágenes)
# URL: http://127.0.0.1:5000/frutas
# ==========================================

@app.route("/frutas")
def catalogo():
    """
    Segunda ruta: Renderiza 'frutas.html', que muestra la vista de tarjetas
    con imágenes de las frutas y la sección '¿Por qué elegirnos?'.
    """
    return render_template(
        "frutas.html",
        frutas=frutas
    )

# ==========================================
# TERCERA RUTA: Procesar Compra
# URL: http://127.0.0.1:5000/checkout (Método POST)
# ==========================================

@app.route("/checkout", methods=["POST"])
def checkout():
    # ----------------------------
    # Información del cliente (Uso de .get para mayor seguridad)
    # ----------------------------
    nombre = request.form.get("nombre", "")
    email = request.form.get("email", "")
    direccion = request.form.get("direccion", "")

    # ----------------------------
    # Variables auxiliares
    # ----------------------------
    pedido = []
    total = 0
    total_frutas = 0

    # ----------------------------
    # Recorrer todas las frutas
    # ----------------------------
    for fruta in frutas:
        # Convierte a entero la cantidad enviada desde el HTML. 
        # Si la fruta no se envió, asigna valor por defecto 0.
        cantidad_str = request.form.get(fruta["nombre"], "0")
        cantidad = int(cantidad_str) if cantidad_str.isdigit() else 0

        if cantidad > 0:
            subtotal = cantidad * fruta["precio"]
            pedido.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": fruta["imagen"]
            })
            total += subtotal
            total_frutas += cantidad

    # ----------------------------
    # Mostrar resumen en checkout.html
    # ----------------------------
    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        pedido=pedido,
        total=total,
        total_frutas=total_frutas
    )

# ==========================================
# Ejecutar servidor
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)