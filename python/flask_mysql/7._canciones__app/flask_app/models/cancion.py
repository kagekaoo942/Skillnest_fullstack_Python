from flask_app.config.mysqlconnection import connectToMySQL


class Cancion:
    """Representa una canción y los usuarios que la guardaron."""

    def __init__(self, data):
        self.id = data["id"]
        self.titulo = data["titulo"]
        self.artista = data["artista"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.usuarios = []

    @classmethod
    def get_all(cls):
        """Obtiene todas las canciones ordenadas por ID."""
        query = """
            SELECT id, titulo, artista, created_at, updated_at
            FROM canciones
            ORDER BY id;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query)
        return [cls(cancion) for cancion in (resultados or [])]

    @classmethod
    def get_by_id(cls, id):
        """Busca una canción por ID; devuelve None si no existe."""
        query = """
            SELECT id, titulo, artista, created_at, updated_at
            FROM canciones
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query, {"id": id})
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def save(cls, data):
        """Crea una canción y devuelve el ID generado por MySQL."""
        query = """
            INSERT INTO canciones (titulo, artista)
            VALUES (%(titulo)s, %(artista)s);
        """
        return connectToMySQL("esquema_canciones").query_db(query, data)

    @classmethod
    def get_by_id_with_users(cls, data):
        """Obtiene una canción y los usuarios que la marcaron favorita."""
        query = """
            SELECT
                canciones.id AS cancion_id,
                canciones.titulo AS cancion_titulo,
                canciones.artista AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at,
                usuarios.id AS usuario_id,
                usuarios.nombre AS usuario_nombre,
                usuarios.email AS usuario_email,
                usuarios.created_at AS usuario_created_at,
                usuarios.updated_at AS usuario_updated_at
            FROM canciones
            LEFT JOIN favoritos
                ON favoritos.cancion_id = canciones.id
            LEFT JOIN usuarios
                ON favoritos.usuario_id = usuarios.id
            WHERE canciones.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query, data)
        if not resultados:
            return None

        primera_fila = resultados[0]
        cancion = cls({
            "id": primera_fila["cancion_id"],
            "titulo": primera_fila["cancion_titulo"],
            "artista": primera_fila["cancion_artista"],
            "created_at": primera_fila["cancion_created_at"],
            "updated_at": primera_fila["cancion_updated_at"],
        })

        for fila in resultados:
            if fila["usuario_id"] is not None:
                cancion.usuarios.append({
                    "id": fila["usuario_id"],
                    "nombre": fila["usuario_nombre"],
                    "email": fila["usuario_email"],
                    "created_at": fila["usuario_created_at"],
                    "updated_at": fila["usuario_updated_at"],
                })

        return cancion

    @classmethod
    def get_users_not_favorited(cls, data):
        """Devuelve solo usuarios que aún no tienen favorita la canción."""
        query = """
            SELECT
                usuarios.id,
                usuarios.nombre,
                usuarios.email,
                usuarios.created_at,
                usuarios.updated_at
            FROM usuarios
            LEFT JOIN favoritos
                ON favoritos.usuario_id = usuarios.id
                AND favoritos.cancion_id = %(cancion_id)s
            WHERE favoritos.usuario_id IS NULL
            ORDER BY usuarios.nombre;
        """
        resultados = connectToMySQL("esquema_canciones").query_db(query, data)
        return resultados or []
