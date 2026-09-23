from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    """Representa un usuario y concentra sus consultas CRUD."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Devuelve todos los usuarios ordenados por identificador."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY id;
        """

        resultados = connectToMySQL("crud_usuarios").query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def get_by_id(cls, id):
        """Busca un usuario por ID con una consulta parametrizada."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """

        data = {
            "id": id
        }

        resultados = connectToMySQL("crud_usuarios").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None

    @classmethod
    def save(cls, data):
        """Crea un usuario y devuelve el ID generado por MySQL."""
        query = """
            INSERT INTO usuarios
            (nombre, apellido, email, created_at, updated_at)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """

        return connectToMySQL("crud_usuarios").query_db(query, data)

    @classmethod
    def update(cls, data):
        """Actualiza los datos del usuario indicado."""
        query = """
            UPDATE usuarios
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """

        return connectToMySQL("crud_usuarios").query_db(query, data)

    @classmethod
    def delete(cls, data):
        """Elimina un usuario usando su ID."""
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """

        return connectToMySQL("crud_usuarios").query_db(query, data)
