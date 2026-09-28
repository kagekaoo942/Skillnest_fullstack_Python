import os

import pymysql.cursors


class MySQLConnection:
    """Administra una conexión MySQL y ejecuta consultas parametrizadas."""

    def __init__(self, db):
        self.db = db
        self.connection = None

    def query_db(self, query, data=None):
        """Ejecuta la consulta y devuelve resultados según el tipo de SQL."""
        try:
            self.connection = pymysql.connect(
                host=os.getenv("MYSQL_HOST", "localhost"),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", ""),
                database=self.db,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True,
            )

            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                tipo_consulta = query.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()

                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount
        except Exception as error:
            print("Error al ejecutar una consulta MySQL:", error)
            return False
        finally:
            if self.connection:
                self.connection.close()


def connectToMySQL(db):
    """Crea una instancia de conexión para la base indicada."""
    return MySQLConnection(db)
