from flask_app.config.mysqlconnection import connectToMySQL


class Favorito:
    """Acceso a la relación muchos-a-muchos entre usuarios y libros."""

    @classmethod
    def existe(cls, usuario_id, libro_id):
        query = """
            SELECT usuario_id
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s AND libro_id = %(libro_id)s
            LIMIT 1;
        """
        resultados = connectToMySQL().query_db(
            query, {"usuario_id": usuario_id, "libro_id": libro_id}
        )
        if resultados is False:
            return None
        return bool(resultados)

    @classmethod
    def agregar(cls, usuario_id, libro_id):
        """Inserta una sola relación; duplicados son idempotentes."""
        query = """
            INSERT IGNORE INTO favoritos (usuario_id, libro_id)
            VALUES (%(usuario_id)s, %(libro_id)s);
        """
        return connectToMySQL().query_db(
            query, {"usuario_id": usuario_id, "libro_id": libro_id}
        )

    @classmethod
    def obtener_usuarios(cls, libro_id):
        query = """
            SELECT u.id, u.nombre, u.apellido
            FROM favoritos AS f
            INNER JOIN usuarios AS u ON u.id = f.usuario_id
            WHERE f.libro_id = %(libro_id)s
            ORDER BY u.nombre, u.apellido
            -- El detalle solo presenta una muestra de usuarios para mantener la lista compacta.
            LIMIT 12;
        """
        resultados = connectToMySQL().query_db(query, {"libro_id": libro_id})
        if resultados is False:
            return False
        return resultados
