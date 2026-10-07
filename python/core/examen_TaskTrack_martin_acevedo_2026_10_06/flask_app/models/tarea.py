from flask_app.config.mysqlconnection import query_db


class Tarea:
    @staticmethod
    def listar(usuario_id):
        return query_db(
            """
            SELECT t.*, c.nombre AS categoria_nombre
            FROM tareas t
            JOIN categorias c ON c.id = t.categoria_id
            WHERE c.usuario_id = %(usuario_id)s
            ORDER BY t.fecha_limite IS NULL, t.fecha_limite
            """,
            {"usuario_id": usuario_id},
        )

    @staticmethod
    def proximas(usuario_id):
        return query_db(
            """
            SELECT t.*, DATEDIFF(t.fecha_limite, CURDATE()) AS dias_restantes
            FROM tareas t
            JOIN categorias c ON c.id = t.categoria_id
            WHERE c.usuario_id = %(usuario_id)s
              AND t.estado <> 'Completada'
              AND t.fecha_limite IS NOT NULL
            ORDER BY t.fecha_limite
            LIMIT 5
            """,
            {"usuario_id": usuario_id},
        )

    @staticmethod
    def resumen(usuario_id):
        row = query_db(
            """
            SELECT COUNT(*) AS total,
                SUM(estado = 'Pendiente') AS pendientes,
                SUM(estado = 'En progreso') AS en_progreso,
                SUM(estado = 'Completada') AS completadas
            FROM tareas t
            JOIN categorias c ON c.id = t.categoria_id
            WHERE c.usuario_id = %(usuario_id)s
            """,
            {"usuario_id": usuario_id},
            fetch="one",
        )
        return row or {"total": 0, "pendientes": 0, "en_progreso": 0, "completadas": 0}

    @staticmethod
    def buscar(tarea_id, usuario_id):
        return query_db(
            """
            SELECT t.*, c.nombre AS categoria_nombre,
                   CONCAT(u.nombre, ' ', u.apellido) AS creador_nombre
            FROM tareas t
            JOIN categorias c ON c.id = t.categoria_id
            JOIN usuarios u ON u.id = c.usuario_id
            WHERE t.id = %(id)s AND c.usuario_id = %(usuario_id)s
            """,
            {"id": tarea_id, "usuario_id": usuario_id},
            fetch="one",
        )

    @staticmethod
    def crear(datos):
        return query_db(
            """
            INSERT INTO tareas
                (titulo, categoria_id, prioridad, fecha_limite, descripcion)
            VALUES
                (%(titulo)s, %(categoria_id)s, %(prioridad)s, %(fecha_limite)s,
                 %(descripcion)s)
            """,
            datos,
            fetch="none",
        )

    @staticmethod
    def actualizar(tarea_id, usuario_id, datos):
        datos.update({"id": tarea_id, "usuario_id": usuario_id})
        return query_db(
            """
            UPDATE tareas
            SET titulo = %(titulo)s, categoria_id = %(categoria_id)s,
                prioridad = %(prioridad)s, fecha_limite = %(fecha_limite)s,
                descripcion = %(descripcion)s
            WHERE id = %(id)s
              AND categoria_id IN (
                  SELECT id FROM categorias WHERE usuario_id = %(usuario_id)s
              )
            """,
            datos,
            fetch="none",
        )

    @staticmethod
    def eliminar(tarea_id, usuario_id):
        return query_db(
            """
            DELETE t FROM tareas t
            JOIN categorias c ON c.id = t.categoria_id
            WHERE t.id = %(id)s AND c.usuario_id = %(usuario_id)s
            """,
            {"id": tarea_id, "usuario_id": usuario_id},
            fetch="none",
        )
