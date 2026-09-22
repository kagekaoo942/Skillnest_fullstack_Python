from mysqlconnection import connectToMySQL


class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            ORDER BY id_estudiante;
        """
        resultados = connectToMySQL("esquema_estudiantes").query_db(query)
        return [cls(estudiante) for estudiante in (resultados or [])]

    @classmethod
    def get_by_id(cls, id_estudiante):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
        """
        resultados = connectToMySQL("esquema_estudiantes").query_db(
            query,
            {"id_estudiante": id_estudiante},
        )
        return cls(resultados[0]) if resultados else None

    @classmethod
    def actualizar(cls, data):
        query = """
            UPDATE estudiantes
            SET nombre = %(nombre)s,
                email = %(email)s
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = """
            DELETE FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)
