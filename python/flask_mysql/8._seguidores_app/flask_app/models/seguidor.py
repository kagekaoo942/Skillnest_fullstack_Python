from flask_app.config.mysqlconnection import connectToMySQL


DATABASE = "esquema_seguidores"


class Seguidor:
    """Gestiona las relaciones entre dos registros de usuarios."""

    @classmethod
    def get_all(cls):
        """Devuelve las relaciones usando usuarios en dos roles distintos."""
        query = """
            SELECT
                u.id AS usuario_id,
                CONCAT(u.nombre, ' ', u.apellido) AS usuario_nombre,
                s.id AS seguidor_id,
                CONCAT(s.nombre, ' ', s.apellido) AS seguidor_nombre
            FROM seguidores AS f
            INNER JOIN usuarios AS u ON f.usuario_id = u.id
            INNER JOIN usuarios AS s ON f.seguidor_id = s.id
            ORDER BY u.nombre, u.apellido, s.nombre, s.apellido;
        """
        resultados = connectToMySQL(DATABASE).query_db(query)
        return None if resultados is False else resultados

    @classmethod
    def existe(cls, data):
        """Comprueba si ya se guardó el par usuario-seguidor."""
        query = """
            SELECT id
            FROM seguidores
            WHERE usuario_id = %(usuario_id)s
              AND seguidor_id = %(seguidor_id)s;
        """
        resultados = connectToMySQL(DATABASE).query_db(query, data)

        if resultados is False:
            return None

        return bool(resultados)

    @classmethod
    def seguir(cls, data):
        """Crea la relación; la restricción UNIQUE también protege duplicados."""
        query = """
            INSERT INTO seguidores (usuario_id, seguidor_id)
            VALUES (%(usuario_id)s, %(seguidor_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
