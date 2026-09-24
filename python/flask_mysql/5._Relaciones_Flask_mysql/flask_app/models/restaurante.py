from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.taco import Taco


class Restaurante:
    """Representa un restaurante y los objetos Taco que le pertenecen."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # La consulta de detalle llena esta lista con objetos Taco.
        self.tacos = []

    @classmethod
    def save(cls, datos):
        """Crea un restaurante."""
        query = """
            INSERT INTO restaurantes (nombre)
            VALUES (%(nombre)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_all(cls):
        """Obtiene todos los restaurantes disponibles."""
        query = """
            SELECT id, nombre, created_at, updated_at
            FROM restaurantes
            ORDER BY id;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query)
        if not resultados:
            return []
        return [cls(restaurante) for restaurante in resultados]

    @classmethod
    def get_restaurante_y_tacos(cls, datos):
        """Agrupa los resultados de LEFT JOIN en un Restaurante y sus tacos."""
        query = """
            SELECT
                restaurantes.id AS restaurante_id,
                restaurantes.nombre AS restaurante_nombre,
                restaurantes.created_at AS restaurante_created_at,
                restaurantes.updated_at AS restaurante_updated_at,
                tacos.id AS taco_id,
                tacos.tortilla AS taco_tortilla,
                tacos.guiso AS taco_guiso,
                tacos.salsa AS taco_salsa,
                tacos.restaurante_id AS taco_restaurante_id,
                tacos.created_at AS taco_created_at,
                tacos.updated_at AS taco_updated_at
            FROM restaurantes
            LEFT JOIN tacos
                ON tacos.restaurante_id = restaurantes.id
            WHERE restaurantes.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query, datos)
        if not resultados:
            return None

        primera_fila = resultados[0]
        restaurante = cls({
            "id": primera_fila["restaurante_id"],
            "nombre": primera_fila["restaurante_nombre"],
            "created_at": primera_fila["restaurante_created_at"],
            "updated_at": primera_fila["restaurante_updated_at"]
        })

        # LEFT JOIN devuelve taco_id=None si el restaurante no tiene tacos.
        for fila in resultados:
            if fila["taco_id"] is None:
                continue

            restaurante.tacos.append(Taco({
                "id": fila["taco_id"],
                "tortilla": fila["taco_tortilla"],
                "guiso": fila["taco_guiso"],
                "salsa": fila["taco_salsa"],
                "restaurante_id": fila["taco_restaurante_id"],
                "created_at": fila["taco_created_at"],
                "updated_at": fila["taco_updated_at"]
            }))

        return restaurante
