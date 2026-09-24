from flask_app.config.mysqlconnection import connectToMySQL


class Curso:
    """Representa un registro de la tabla cursos."""

    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre_curso = data["nombre_curso"]
        self.descripcion = data["descripcion"]
        self.created_at = data["created_at"]

    @classmethod
    def get_all(cls):
        """Obtiene todos los cursos ordenados por identificador."""
        query = """
            SELECT id_curso, nombre_curso, descripcion, created_at
            FROM cursos
            ORDER BY id_curso;
        """
        resultados = connectToMySQL("esquema_educacion").query_db(query)
        if not resultados:
            return []
        return [cls(curso) for curso in resultados]

    @classmethod
    def get_by_id(cls, id_curso):
        """Busca un curso por ID; devuelve None si no existe."""
        query = """
            SELECT id_curso, nombre_curso, descripcion, created_at
            FROM cursos
            WHERE id_curso = %(id_curso)s;
        """
        data = {"id_curso": id_curso}
        resultados = connectToMySQL("esquema_educacion").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None
