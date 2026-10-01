import re

from flask_login import UserMixin

from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


class Usuario(UserMixin):
    """Cuenta autenticable que guarda únicamente el hash de la contraseña."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password_hash = data["password_hash"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}".strip()

    @staticmethod
    def validar(datos):
        errores = []
        nombre = (datos.get("nombre") or "").strip()
        apellido = (datos.get("apellido") or "").strip()
        # El correo se normaliza para evitar cuentas duplicadas por diferencias de mayúsculas.
        email = (datos.get("email") or "").strip().lower()
        password = datos.get("password") or ""
        confirmar_password = datos.get("confirmar_password") or ""

        if len(nombre) < 2 or len(nombre) > 80:
            errores.append("El nombre debe tener al menos 2 caracteres.")
        if len(apellido) < 2 or len(apellido) > 80:
            errores.append("El apellido debe tener al menos 2 caracteres.")
        if len(email) > 150 or not EMAIL_REGEX.fullmatch(email):
            errores.append("Escribe un correo electrónico válido.")
        if len(password) < 8 or len(password) > 72:
            errores.append("La contraseña debe tener entre 8 y 72 caracteres.")
        if password != confirmar_password:
            errores.append("La contraseña y su confirmación deben coincidir.")

        return errores

    @classmethod
    def crear(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password_hash)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password_hash)s);
        """
        return connectToMySQL().query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, email):
        query = """
            SELECT id, nombre, apellido, email, password_hash, created_at, updated_at
            FROM usuarios WHERE email = %(email)s LIMIT 1;
        """
        resultados = connectToMySQL().query_db(query, {"email": email.strip().lower()})
        if resultados is False:
            return False
        return cls(resultados[0]) if resultados else None

    @classmethod
    def buscar_por_id(cls, usuario_id):
        query = """
            SELECT id, nombre, apellido, email, password_hash, created_at, updated_at
            FROM usuarios WHERE id = %(id)s LIMIT 1;
        """
        resultados = connectToMySQL().query_db(query, {"id": usuario_id})
        if resultados is False:
            return None
        return cls(resultados[0]) if resultados else None
