# conexion.py
import mysql.connector

def ejecutar_sql(query, valores=()):
    """Abre la BD, ejecuta el comando SQL, guarda los cambios y cierra todo."""
    db = mysql.connector.connect(
        host='localhost', 
        user='root',         
        password='1234',      # Tu contraseña real de la base de datos
        database='usuarios_db' 
    )
    cursor = db.cursor()
    
    cursor.execute(query, valores)
    
    # Si es una consulta que devuelve filas (como SELECT), las extrae
    resultado = cursor.fetchall() if cursor.with_rows else None
    
    db.commit()
    cursor.close()
    db.close()
    
    return resultado