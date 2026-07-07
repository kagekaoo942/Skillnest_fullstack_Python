# usuario.py
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
    
    query = """
        SELECT u.id, u.usuario, IF(t.nombre_tipo = 'Administrador', 'ADMIN', 'USER') 
        FROM usuarios u 
        JOIN tipos_usuario t ON u.tipo_usuario = t.id
    """
    usuarios = ejecutar_sql(query)
    
    for fila in usuarios:
        print(fila[0], "|", fila[1], "|", fila[2])

def buscar_usuario():
    print("\n--- 3. BUSCAR USUARIO ---")
    id_buscar = input("Solicitar ID: ")
    
    query = """
        SELECT u.id, u.usuario, u.password, IF(t.nombre_tipo = 'Administrador', 'ADMIN', 'USER') 
        FROM usuarios u 
        JOIN tipos_usuario t ON u.tipo_usuario = t.id 
        WHERE u.id = %s
    """
    resultado = ejecutar_sql(query, (id_buscar,))
    
    if resultado:
        fila = resultado[0]
        print("\nInformación encontrada:")
        print("ID:", fila[0])
        print("Usuario:", fila[1])
        print("Contraseña:", fila[2])
        print("Tipo:", fila[3])
    else:
        print("❌ Usuario no encontrado.")

def modificar_usuario():
    print("\n--- 4. MODIFICAR USUARIO ---")
    id_modificar = input("Solicitar ID: ")
    
    existe = ejecutar_sql("SELECT id FROM usuarios WHERE id = %s", (id_modificar,))
    if not existe:
        print("❌ El ID no existe.")
        return
        
    nuevo_usuario = input("Nuevo usuario: ")
    nuevo_password = input("Nueva contraseña: ")
    nuevo_tipo = input("Nuevo tipo (1 para ADMIN, 2 para USER): ")
    
    query = "UPDATE usuarios SET usuario = %s, password = %s, tipo_usuario = %s WHERE id = %s"
    ejecutar_sql(query, (nuevo_usuario, nuevo_password, nuevo_tipo, id_modificar))
    print("✔️ Usuario actualizado con éxito.")

def eliminar_usuario():
    print("\n--- 5. ELIMINAR USUARIO ---")
    id_eliminar = input("Solicitar ID: ")
    
    existe = ejecutar_sql("SELECT id FROM usuarios WHERE id = %s", (id_eliminar,))
    if not existe:
        print("❌ El ID no existe.")
        return
        
    ejecutar_sql("DELETE FROM usuarios WHERE id = %s", (id_eliminar,))
    print("✔️ Registro eliminado correctamente.")