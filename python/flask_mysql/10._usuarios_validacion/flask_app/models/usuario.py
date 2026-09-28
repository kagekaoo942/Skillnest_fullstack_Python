import re

from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


class Usuario:
    """Representa un registro de la tabla usuarios."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(usuario):
        """Valida los campos requeridos y el formato básico del correo."""
        es_valido = True
        nombre = (usuario.get("nombre") or "").strip()
        apellido = (usuario.get("apellido") or "").strip()
        email = (usuario.get("email") or "").strip()

        if not nombre:
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False

        if not apellido:
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False

        if not email:
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(email):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False

        return es_valido

    @classmethod
    def get_all(cls):
        """Obtiene usuarios en orden descendente de identificador."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY id DESC;
        """
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        return [cls(usuario) for usuario in (resultados or [])]

    @classmethod
    def get_by_id(cls, id):
        """Busca un usuario por su identificador; retorna None si no existe."""
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL("esquema_usuarios").query_db(query, {"id": id})

        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def email_existe(cls, email):
        """Comprueba si el correo ya está asociado a un usuario."""
        query = """
            SELECT id
            FROM usuarios
            WHERE email = %(email)s;
        """
        resultados = connectToMySQL("esquema_usuarios").query_db(
            query,
            {"email": email},
        )
        return bool(resultados)

    @classmethod
    def save(cls, data):
        """Inserta un usuario con una sentencia preparada."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL("esquema_usuarios").query_db(query, data)
