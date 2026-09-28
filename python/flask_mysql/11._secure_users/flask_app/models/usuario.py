import re

from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
)


class Usuario:
    """Representa un usuario; password contiene solo el hash Bcrypt."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(datos):
        """Comprueba nombre, apellido, email y contraseña antes de guardar."""
        es_valido = True
        nombre = (datos.get("nombre") or "").strip()
        apellido = (datos.get("apellido") or "").strip()
        email = (datos.get("email") or "").strip()
        password = datos.get("password") or ""

        if not nombre:
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False
        elif len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "nombre")
            es_valido = False

        if not apellido:
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False
        elif len(apellido) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "apellido")
            es_valido = False

        if not email:
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(email):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False

        if not password:
            flash("La contraseña es obligatoria.", "password")
            es_valido = False
        elif len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "password")
            es_valido = False

        return es_valido

    @classmethod
    def guardar(cls, datos):
        """Inserta los datos validados; la contraseña recibida debe ser un hash."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL().query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, datos):
        """Busca una cuenta por correo y retorna None si no se encontró."""
        query = """
            SELECT id, nombre, apellido, email, password, created_at, updated_at
            FROM usuarios
            WHERE email = %(email)s;
        """
        resultados = connectToMySQL().query_db(query, datos)

        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return None

    @classmethod
    def buscar_por_id(cls, datos):
        """Obtiene el usuario que pertenece al identificador de sesión."""
        query = """
            SELECT id, nombre, apellido, email, password, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL().query_db(query, datos)

        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return None

    @classmethod
    def existe_email(cls, datos):
        """Comprueba disponibilidad del email antes de intentar la inserción."""
        query = """
            SELECT id
            FROM usuarios
            WHERE email = %(email)s;
        """
        resultados = connectToMySQL().query_db(query, datos)
        return bool(resultados)
