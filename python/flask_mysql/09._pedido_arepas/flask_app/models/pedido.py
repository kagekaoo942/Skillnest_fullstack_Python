from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL


class Pedido:
    """Representa un registro de la tabla pedidos."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo_arepa = data["tipo_arepa"]
        self.cantidad = data["cantidad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_pedido(pedido):
        """Valida campos requeridos, longitud del nombre y cantidad positiva."""
        es_valido = True
        nombre = (pedido.get("nombre") or "").strip()
        tipo_arepa = (pedido.get("tipo_arepa") or "").strip()
        cantidad_texto = (pedido.get("cantidad") or "").strip()

        if not nombre:
            flash("El nombre es obligatorio.", "danger")
            es_valido = False
        elif len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "danger")
            es_valido = False

        if not tipo_arepa:
            flash("El tipo de arepa es obligatorio.", "danger")
            es_valido = False

        if not cantidad_texto:
            flash("La cantidad es obligatoria.", "danger")
            es_valido = False
        else:
            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                flash("La cantidad debe ser mayor que 0.", "danger")
                es_valido = False
            else:
                if cantidad <= 0:
                    flash("La cantidad debe ser mayor que 0.", "danger")
                    es_valido = False

        return es_valido

    @classmethod
    def get_all(cls):
        """Obtiene los pedidos en orden descendente de creación."""
        query = """
            SELECT id, nombre, tipo_arepa, cantidad, created_at, updated_at
            FROM pedidos
            ORDER BY id DESC;
        """
        resultados = connectToMySQL("esquema_arepas").query_db(query)
        return [cls(pedido) for pedido in (resultados or [])]

    @classmethod
    def save(cls, data):
        """Inserta un pedido mediante una sentencia preparada."""
        query = """
            INSERT INTO pedidos (nombre, tipo_arepa, cantidad)
            VALUES (%(nombre)s, %(tipo_arepa)s, %(cantidad)s);
        """
        return connectToMySQL("esquema_arepas").query_db(query, data)
