import mysql.connector

def ejecutar_sql(query, valores=()):
    # VERIFICA ESTOS 4 DATOS:
    db = mysql.connector.connect(
        host='localhost', 
        user='root',         # Tu usuario de MySQL
        password='1234',         #contraseña
        database='usuarios_db' # El nombre exacto de tu base de datos
    )
    cursor = db.cursor()
    cursor.execute(query, valores)
    resultado = cursor.fetchall() if cursor.with_rows else None
    db.commit()
    cursor.close()
    db.close()
    return resultado