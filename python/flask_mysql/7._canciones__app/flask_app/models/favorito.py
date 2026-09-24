from flask_app.config.mysqlconnection import connectToMySQL


class Favorito:
    """Representa la relación entre un usuario y una canción."""

    @classmethod
    def existe(cls, data):
        """Comprueba si ya existe la pareja usuario-canción."""
        query = """
            SELECT usuario_id, cancion_id
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s
              AND cancion_id = %(cancion_id)s;
        """
        resultado = connectToMySQL("esquema_canciones").query_db(query, data)
        return bool(resultado)

    @classmethod
    def agregar(cls, data):
        """Crea la relación; la clave compuesta impide duplicados."""
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id)
            VALUES (%(usuario_id)s, %(cancion_id)s);
        """
        return connectToMySQL("esquema_canciones").query_db(query, data)
