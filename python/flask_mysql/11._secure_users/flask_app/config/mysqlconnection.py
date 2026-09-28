import os

import pymysql
import pymysql.cursors


class MySQLConnection:
    """Abre una conexión MySQL por consulta y devuelve resultados simples."""

    def __init__(self, db):
        self.db = db

    def query_db(self, query, data=None):
        """SELECT devuelve filas; INSERT devuelve id; los errores devuelven False."""
        connection = None
        try:
            connection = pymysql.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=self.db,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True,
            )

            with connection.cursor() as cursor:
                cursor.execute(query, data or {})
                tipo_consulta = query.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()

                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount
        except (pymysql.MySQLError, OSError) as error:
            print(f"Error MySQL: {error}")
            return False
        finally:
            if connection is not None:
                connection.close()


def connectToMySQL(db=None):
    """Crea una conexión usando DB_NAME cuando no se indica otra base."""
    return MySQLConnection(db or os.getenv("DB_NAME", "esquema_loginreg"))
