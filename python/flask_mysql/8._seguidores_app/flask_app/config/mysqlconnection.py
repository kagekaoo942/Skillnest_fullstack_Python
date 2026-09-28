import logging
import os

import pymysql
import pymysql.cursors


logger = logging.getLogger(__name__)


class MySQLConnection:
    """Abre una conexión MySQL por consulta y devuelve resultados sencillos."""

    def __init__(self, db):
        self.db = db

    def query_db(self, query, data=None):
        connection = None

        try:
            connection = pymysql.connect(
                host=os.environ.get("MYSQL_HOST", "localhost"),
                user=os.environ.get("MYSQL_USER", "root"),
                password=os.environ.get("MYSQL_PASSWORD", ""),
                port=int(os.environ.get("MYSQL_PORT", "3306")),
                database=self.db,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True,
                connect_timeout=5,
            )

            with connection.cursor() as cursor:
                cursor.execute(query, data)
                query_type = query.strip().lower()

                if query_type.startswith("select"):
                    return cursor.fetchall()

                if query_type.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount

        except (pymysql.MySQLError, OSError, ValueError):
            logger.exception("No se pudo ejecutar la consulta en MySQL.")
            return False
        finally:
            if connection is not None:
                connection.close()


def connectToMySQL(db):
    """Crea un ejecutor de consultas preparado para la base indicada."""
    return MySQLConnection(db)
