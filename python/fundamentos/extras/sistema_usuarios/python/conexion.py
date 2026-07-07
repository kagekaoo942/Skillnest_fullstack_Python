import mysql.connector

try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',          # Tu usuario de MySQL (por defecto suele ser 'root')
            password='1234',    # Tu contraseña de MySQL
            database='usuarios_db'       # El nombre de tu base de datos
        )
        cursor = conexion.cursor()
        print("conexion exitosa")

except Exception as e:
        print(f"Error al conectar a MySQL: {e}")