from datetime import date

from flask_app.config.mysqlconnection import connectToMySQL


GENEROS_LIBRO = (
    "Novela",
    "Fábula",
    "Ciencia Ficción",
    "Romance",
    "Desarrollo Personal",
    "Álbum Infantil",
    "Fantasía",
    "Historia",
    "Poesía",
    "Otro",
)
# límites que tiene el selector de fecha del formulario.
FECHA_PUBLICACION_MINIMA = date(2020, 1, 1)
FECHA_PUBLICACION_MAXIMA = date(2026, 12, 31)


class Libro:
    """Libro propio o visible a la comunidad."""

    def __init__(self, data):
        self.id = data["id"]
        self.usuario_id = data["usuario_id"]
        self.titulo = data["titulo"]
        self.autor = data["autor"]
        self.genero = data["genero"]
        self.fecha_publicacion = data["fecha_publicacion"]
        self.descripcion = data["descripcion"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.publicado_por = data.get("publicado_por", "")
        self.favoritos = int(data.get("favoritos", 0) or 0)

    @staticmethod
    def validar(datos):
        """Aplica las mismas reglas en alta y edición."""
        errores = []
        titulo = (datos.get("titulo") or "").strip()
        autor = (datos.get("autor") or "").strip()
        genero = (datos.get("genero") or "").strip()
        fecha_texto = (datos.get("fecha_publicacion") or "").strip()
        descripcion = (datos.get("descripcion") or "").strip()

        if len(titulo) < 2:
            errores.append("El título debe tener al menos 2 caracteres.")
        elif len(titulo) > 180:
            errores.append("El título no puede superar 180 caracteres.")
        if not autor:
            errores.append("Introduce el autor.")
        elif len(autor) > 120:
            errores.append("El autor no puede superar 120 caracteres.")
        if genero not in GENEROS_LIBRO:
            errores.append("Selecciona un género válido.")
        try:
            fecha_publicacion = date.fromisoformat(fecha_texto)
        except ValueError:
            fecha_publicacion = None
            errores.append("Introduce una fecha de publicación válida.")
        else:
            if not FECHA_PUBLICACION_MINIMA <= fecha_publicacion <= FECHA_PUBLICACION_MAXIMA:
                errores.append("La fecha de publicación debe estar entre 2020 y 2026.")
        if len(descripcion) < 10:
            errores.append("La descripción debe tener al menos 10 caracteres.")
        elif len(descripcion) > 5000:
            errores.append("La descripción no puede superar 5000 caracteres.")

        return {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "fecha_publicacion": fecha_publicacion,
            "descripcion": descripcion,
        }, errores

    @classmethod
    def obtener_todos_del_usuario(cls, usuario_id):
        query = """
            SELECT l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                   l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                   COUNT(f.usuario_id) AS favoritos
            FROM libros AS l
            LEFT JOIN favoritos AS f ON f.libro_id = l.id
            WHERE l.usuario_id = %(usuario_id)s
            GROUP BY l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                     l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at
            ORDER BY l.titulo, l.id;
        """
        resultados = connectToMySQL().query_db(query, {"usuario_id": usuario_id})
        if resultados is False:
            return False
        return [cls(fila) for fila in resultados]

    @classmethod
    def obtener_comunidad(cls, usuario_id):
        """Devuelve libros ajenos publicados para la comunidad."""
        query = """
            SELECT l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                   l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                   CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   COUNT(f.usuario_id) AS favoritos
            FROM libros AS l
            INNER JOIN usuarios AS u ON u.id = l.usuario_id
            LEFT JOIN favoritos AS f ON f.libro_id = l.id
            WHERE l.usuario_id <> %(usuario_id)s
            GROUP BY l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                     l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                     u.nombre, u.apellido
            ORDER BY l.created_at DESC, l.id DESC;
        """
        resultados = connectToMySQL().query_db(query, {"usuario_id": usuario_id})
        if resultados is False:
            return False
        return [cls(fila) for fila in resultados]

    @classmethod
    def obtener_propietario(cls, libro_id, usuario_id):
        query = """
            SELECT id, usuario_id, titulo, autor, genero, fecha_publicacion,
                   descripcion, created_at, updated_at
            FROM libros
            WHERE id = %(id)s AND usuario_id = %(usuario_id)s
            LIMIT 1;
        """
        resultados = connectToMySQL().query_db(
            query, {"id": libro_id, "usuario_id": usuario_id}
        )
        if resultados is False:
            return False
        return cls(resultados[0]) if resultados else None

    @classmethod
    def obtener_visible(cls, libro_id):
        """Detalle visible a cualquier usuario autenticado."""
        query = """
            SELECT l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                   l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                   CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   COUNT(f.usuario_id) AS favoritos
            FROM libros AS l
            INNER JOIN usuarios AS u ON u.id = l.usuario_id
            LEFT JOIN favoritos AS f ON f.libro_id = l.id
            WHERE l.id = %(id)s
            GROUP BY l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                     l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                     u.nombre, u.apellido
            LIMIT 1;
        """
        resultados = connectToMySQL().query_db(query, {"id": libro_id})
        if resultados is False:
            return False
        return cls(resultados[0]) if resultados else None

    @classmethod
    def obtener_favoritos_del_usuario(cls, usuario_id):
        query = """
            SELECT l.id, l.usuario_id, l.titulo, l.autor, l.genero,
                   l.fecha_publicacion, l.descripcion, l.created_at, l.updated_at,
                   CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   (SELECT COUNT(*) FROM favoritos AS fc WHERE fc.libro_id = l.id) AS favoritos
            FROM favoritos AS f
            INNER JOIN libros AS l ON l.id = f.libro_id
            INNER JOIN usuarios AS u ON u.id = l.usuario_id
            WHERE f.usuario_id = %(usuario_id)s
            ORDER BY f.created_at DESC, l.titulo;
        """
        resultados = connectToMySQL().query_db(query, {"usuario_id": usuario_id})
        if resultados is False:
            return False
        return [cls(fila) for fila in resultados]

    @classmethod
    def crear(cls, usuario_id, datos):
        query = """
            INSERT INTO libros
                (usuario_id, titulo, autor, genero, fecha_publicacion, descripcion)
            VALUES
                (%(usuario_id)s, %(titulo)s, %(autor)s, %(genero)s,
                 %(fecha_publicacion)s, %(descripcion)s);
        """
        return connectToMySQL().query_db(query, {**datos, "usuario_id": usuario_id})

    @classmethod
    def actualizar_propietario(cls, libro_id, usuario_id, datos):
        query = """
            UPDATE libros
            SET titulo = %(titulo)s,
                autor = %(autor)s,
                genero = %(genero)s,
                fecha_publicacion = %(fecha_publicacion)s,
                descripcion = %(descripcion)s
            WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
        """
        values = {**datos, "id": libro_id, "usuario_id": usuario_id}
        return connectToMySQL().query_db(query, values)

    @classmethod
    def eliminar_propietario(cls, libro_id, usuario_id):
        query = "DELETE FROM libros WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL().query_db(
            query, {"id": libro_id, "usuario_id": usuario_id}
        )
