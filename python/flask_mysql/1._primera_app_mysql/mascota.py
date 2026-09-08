# ==========================================================
# MODELO MASCOTA
# ==========================================================
#
# Este archivo representa la tabla "mascotas"
# mediante una clase de Python.
#
# ==========================================================


# Importamos la función encargada de crear
# una conexión con MySQL.

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus datos en atributos del objeto.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas almacenadas
        en la base de datos.

        Retorna una lista de objetos Mascota.
        """

        # --------------------------------------------------
        # Consulta SQL
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas;
        """


        # --------------------------------------------------
        # Ejecutar consulta
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        # --------------------------------------------------
        # Crear lista de objetos
        # --------------------------------------------------

        mascotas = []


        # --------------------------------------------------
        # Convertir cada diccionario en Mascota
        # --------------------------------------------------

        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        # --------------------------------------------------
        # Retornar resultado
        # --------------------------------------------------

        return mascotas

    @classmethod
    def get_by_id(cls, id_mascota):
        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """
        data = {"id_mascota": id_mascota}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_by_name(cls, nombre):
        query = """
            SELECT *
            FROM mascotas
            WHERE nombre = %(nombre_mascota)s;
        """
        data = {"nombre_mascota": nombre}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_by_tipo(cls, tipo):
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo_mascota)s;
        """
        data = {"tipo_mascota": tipo}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        return [cls(mascota) for mascota in resultados]
