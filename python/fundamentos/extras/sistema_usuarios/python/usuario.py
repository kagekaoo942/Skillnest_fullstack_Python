from conexion import ejecutar_sql

def registrar_usuario():
    print("\n--- 1. REGISTRAR ---")
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    tipo = input("Tipo (1 para ADMIN, 2 para USER): ")
    
    ejecutar_sql("INSERT INTO usuarios (usuario, password, tipo_usuario) VALUES (%s, %s, %s)", (usuario, password, tipo))
    print("✔️ Guardado.")

def listar_usuarios():
    print("\nID | Usuario | Tipo")
    print("-------------------")
    
    # Esta es la consulta simplificada que le pide a MySQL que devuelva 'ADMIN' o 'USER'
    query = """
        SELECT u.id, u.usuario, IF(t.nombre_tipo = 'Administrador', 'ADMIN', 'USER') 
        FROM usuarios u 
        JOIN tipos_usuario t ON u.tipo_usuario = t.id
    """
    usuarios = ejecutar_sql(query)
    
    for fila in usuarios:
        print(fila[0], "|", fila[1], "|", fila[2])