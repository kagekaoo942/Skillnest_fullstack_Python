import pymysql.cursors


class MySQLConnection:
    """Administra una conexión con MySQL y ejecuta consultas preparadas."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta SQL y devuelve filas, ID insertado o filas afectadas."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid or cursor.rowcount

                return cursor.rowcount
        except Exception as error:
            print("Error al ejecutar una consulta MySQL:", error)
            return False
        finally:
            self.connection.close()


def connectToMySQL(db):
    """Crea una conexión con la base de datos especificada."""
    return MySQLConnection(db)
