from flask_app.config.mysqlconnection import connectToMySQL


DATABASE = "esquema_seguidores"


class Usuario:
    """Representa un registro de la tabla usuarios."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Devuelve todos los usuarios ordenados por nombre."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY nombre, apellido, id;
        """
        resultados = connectToMySQL(DATABASE).query_db(query)

        if resultados is False:
            return None

        return [cls(usuario) for usuario in resultados]

    @classmethod
    def get_by_id(cls, id):
        """Busca un usuario por su ID mediante una consulta preparada."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL(DATABASE).query_db(query, {"id": id})

        if resultados is False or not resultados:
            return None

        return cls(resultados[0])

    @classmethod
    def save(cls, data):
        """Inserta un usuario y devuelve el ID generado o False."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
