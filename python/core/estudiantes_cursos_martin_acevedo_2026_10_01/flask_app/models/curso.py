from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante


class Curso:
    """Representa un curso y los estudiantes que tiene asociados."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.estudiantes = []

    @classmethod
    def get_all(cls):
        """Obtiene todos los cursos ordenados por nombre."""
        query = """
            SELECT id, nombre, created_at, updated_at
            FROM cursos
            ORDER BY nombre;
        """
        resultados = connectToMySQL().query_db(query)
        if resultados is False:
            return False
        return [cls(curso) for curso in resultados]

    @classmethod
    def save(cls, data):
        """Guarda un curso nuevo y devuelve su identificador."""
        query = """
            INSERT INTO cursos (nombre)
            VALUES (%(nombre)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def exists(cls, curso_id):
        """Comprueba que el curso seleccionado exista."""
        query = "SELECT id FROM cursos WHERE id = %(id)s;"
        resultados = connectToMySQL().query_db(query, {"id": curso_id})
        if resultados is False:
            return False
        return bool(resultados)

    @classmethod
    def get_curso_con_estudiantes(cls, curso_id):
        """Agrupa un LEFT JOIN en un curso y sus estudiantes."""
        query = """
            SELECT
                c.id AS curso_id,
                c.nombre AS curso_nombre,
                c.created_at AS curso_created_at,
                c.updated_at AS curso_updated_at,
                e.id AS estudiante_id,
                e.nombre AS estudiante_nombre,
                e.apellido AS estudiante_apellido,
                e.edad AS estudiante_edad,
                e.created_at AS estudiante_created_at,
                e.updated_at AS estudiante_updated_at,
                e.curso_id AS estudiante_curso_id
            FROM cursos AS c
            LEFT JOIN estudiantes AS e ON e.curso_id = c.id
            WHERE c.id = %(id)s;
        """
        resultados = connectToMySQL().query_db(query, {"id": curso_id})
        if resultados is False:
            return False
        if not resultados:
            return None

        primera_fila = resultados[0]
        curso = cls({
            "id": primera_fila["curso_id"],
            "nombre": primera_fila["curso_nombre"],
            "created_at": primera_fila["curso_created_at"],
            "updated_at": primera_fila["curso_updated_at"],
        })

        # LEFT JOIN conserva el curso; e.id será NULL si no tiene estudiantes.
        for fila in resultados:
            if fila["estudiante_id"] is None:
                continue

            curso.estudiantes.append(Estudiante({
                "id": fila["estudiante_id"],
                "nombre": fila["estudiante_nombre"],
                "apellido": fila["estudiante_apellido"],
                "edad": fila["estudiante_edad"],
                "created_at": fila["estudiante_created_at"],
                "updated_at": fila["estudiante_updated_at"],
                "curso_id": fila["estudiante_curso_id"],
            }))

        return curso
