from flask_app.config.mysqlconnection import connectToMySQL


class Taco:
    def __init__(self, data):
        self.id = data["id"]
        self.tortilla = data["tortilla"]
        self.guiso = data["guiso"]
        self.salsa = data["salsa"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa, created_at, updated_at)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s, NOW(), NOW());
        """
        return connectToMySQL("esquema_tacos").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            ORDER BY id;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query)
        return [cls(taco) for taco in (resultados or [])]

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query, data)
        return cls(resultados[0]) if resultados else None

    @classmethod
    def update(cls, data):
        query = """
            UPDATE tacos
            SET tortilla = %(tortilla)s,
                guiso = %(guiso)s,
                salsa = %(salsa)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_tacos").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM tacos
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_tacos").query_db(query, data)
