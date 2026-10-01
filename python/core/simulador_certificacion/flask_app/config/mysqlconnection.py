import os

import pymysql
import pymysql.cursors


class ConexionMySQL:
    """Abre una conexión por consulta y normaliza el resultado."""

    def __init__(self, database=None):
        self.database = database or os.getenv("DB_NAME", "bookhub")

    def query_db(self, query, data=None):
        connection = None
        try:
            connection = pymysql.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=self.database,
                charset="utf8mb4",
                # Los modelos acceden a las columnas por nombre, no por posición.
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True,
            )
            with connection.cursor() as cursor:
                cursor.execute(query, data or {})
                # Cada operación devuelve el dato que necesita su modelo llamador.
                query_type = query.lstrip().lower()
                if query_type.startswith("select"):
                    return cursor.fetchall()
                if query_type.startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount
        except (pymysql.MySQLError, OSError) as error:
            print(f"Error MySQL: {error}")
            return False
        finally:
            # La conexión se libera incluso si la ejecución o lectura de resultados falla.
            if connection is not None:
                connection.close()


def connectToMySQL(database=None):
    return ConexionMySQL(database)
