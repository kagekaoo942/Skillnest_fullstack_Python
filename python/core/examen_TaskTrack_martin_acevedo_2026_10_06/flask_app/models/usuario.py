from flask_app.config.mysqlconnection import query_db


class Usuario:
    @staticmethod
    def buscar_por_id(usuario_id):
        return query_db(
            "SELECT id, nombre, apellido, email FROM usuarios "
            "WHERE id = %(id)s",
            {"id": usuario_id},
            fetch="one",
        )

    @staticmethod
    def buscar_por_email(email):
        return query_db(
            "SELECT id, nombre, apellido, email, password FROM usuarios "
            "WHERE email = %(email)s",
            {"email": email},
            fetch="one",
        )

    @staticmethod
    def crear(datos):
        return query_db(
            """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)
            """,
            datos,
            fetch="none",
        )
