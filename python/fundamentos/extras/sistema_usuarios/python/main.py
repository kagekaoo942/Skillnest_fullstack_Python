# main.py
from usuario import registrar_usuario, listar_usuarios, buscar_usuario, modificar_usuario, eliminar_usuario

while True:
    print("\n==============================")
    print("       MENÚ DE OPCIONES       ")
    print("==============================")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Modificar usuario")
    print("5. Eliminar usuario")
    print("6. Cerrar sesión")
    print("==============================")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        listar_usuarios()
    elif opcion == "3":
        buscar_usuario()
    elif opcion == "4":
        modificar_usuario()
    elif opcion == "5":
        eliminar_usuario()
    elif opcion == "6":
        print("Cerrando sesión... Regresando al menú principal.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")