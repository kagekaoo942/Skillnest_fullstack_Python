from flask_app.config.mysqlconnection import connectToMySQL


class Estudiante:
    """Representa un estudiante inscrito en un curso."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.curso_id = data["curso_id"]

    @classmethod
    def save(cls, data):
        """Crea un estudiante asociado al curso indicado."""
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return connectToMySQL().query_db(query, data)
