import pymysql.cursors


class ConexionMySQL:
    """Administra la conexión con MySQL y ejecuta consultas."""

    def __init__(self, db):
        # DictCursor entrega cada fila como un diccionario.
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta una consulta y devuelve filas o el resultado de escritura."""
        with self.connection.cursor() as cursor:
            try:
                # PyMySQL enlaza los datos para evitar concatenarlos al SQL.
                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                # Cada instancia atiende una consulta y luego libera la conexión.
                self.connection.close()


def connectToMySQL(db):
    """Crea una conexión para la base de datos indicada."""
    return ConexionMySQL(db)
