from flask_app.config.mysqlconnection import connectToMySQL


class Inscripcion:
    """Representa el vínculo entre un estudiante y un curso."""

    @classmethod
    def existe(cls, data):
        """Comprueba si ya existe la combinación de IDs."""
        query = """
            SELECT estudiante_id, curso_id
            FROM inscripciones
            WHERE estudiante_id = %(estudiante_id)s
              AND curso_id = %(curso_id)s;
        """
        resultado = connectToMySQL("esquema_educacion").query_db(query, data)
        return bool(resultado)

    @classmethod
    def inscribir_estudiante_en_curso(cls, data):
        """Inserta la relación; la PK compuesta evita duplicados."""
        query = """
            INSERT INTO inscripciones (estudiante_id, curso_id)
            VALUES (%(estudiante_id)s, %(curso_id)s);
        """
        return connectToMySQL("esquema_educacion").query_db(query, data)

    @classmethod
    def get_all(cls):
        """Obtiene las inscripciones con los nombres de ambas entidades."""
        query = """
            SELECT
                estudiantes.id_estudiante,
                estudiantes.nombre AS estudiante,
                estudiantes.email,
                cursos.id_curso,
                cursos.nombre_curso
            FROM inscripciones
            INNER JOIN estudiantes
                ON inscripciones.estudiante_id = estudiantes.id_estudiante
            INNER JOIN cursos
                ON inscripciones.curso_id = cursos.id_curso
            ORDER BY estudiantes.id_estudiante, cursos.id_curso;
        """
        return connectToMySQL("esquema_educacion").query_db(query)
