from flask_app.config.mysqlconnection import query_db


class Categoria:
    @staticmethod
    def buscar(categoria_id, usuario_id):
        return query_db(
            "SELECT id, nombre FROM categorias "
            "WHERE id = %(id)s AND usuario_id = %(usuario_id)s",
            {"id": categoria_id, "usuario_id": usuario_id},
            fetch="one",
        )

    @staticmethod
    def listar_con_tareas(usuario_id):
        return query_db(
            """
            SELECT c.id, c.nombre, COUNT(t.id) AS total_tareas
            FROM categorias c
            LEFT JOIN tareas t ON t.categoria_id = c.id
            WHERE c.usuario_id = %(usuario_id)s
            GROUP BY c.id, c.nombre
            ORDER BY c.nombre
            """,
            {"usuario_id": usuario_id},
        )

    @staticmethod
    def listar(usuario_id):
        return query_db(
            "SELECT id, nombre FROM categorias WHERE usuario_id = %(usuario_id)s "
            "ORDER BY nombre",
            {"usuario_id": usuario_id},
        )

    @staticmethod
    def crear(nombre, usuario_id):
        return query_db(
            "INSERT INTO categorias (nombre, usuario_id) "
            "VALUES (%(nombre)s, %(usuario_id)s)",
            {"nombre": nombre, "usuario_id": usuario_id},
            fetch="none",
        )

    @staticmethod
    def actualizar(categoria_id, usuario_id, nombre):
        return query_db(
            """
            UPDATE categorias
            SET nombre = %(nombre)s
            WHERE id = %(id)s AND usuario_id = %(usuario_id)s
            """,
            {"id": categoria_id, "usuario_id": usuario_id, "nombre": nombre},
            fetch="none",
        )

    @staticmethod
    def eliminar(categoria_id, usuario_id):
        return query_db(
            "DELETE FROM categorias WHERE id = %(id)s AND usuario_id = %(usuario_id)s",
            {"id": categoria_id, "usuario_id": usuario_id},
            fetch="none",
        )
