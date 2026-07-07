# main.py
from usuario import login, registrar_usuario, listar_usuarios, buscar_usuario, modificar_usuario, eliminar_usuario

while True:
    # 1. El sistema siempre pide iniciar sesión al principio
    datos_sesion = login()
    
    if datos_sesion:
        nombre_usuario, tipo_real = datos_sesion
        # Convertimos el tipo que viene de la base de datos a un rol limpio
        rol = "ADMIN" if tipo_real == "Administrador" else "USER"
        
        # 2. MENU SI EL USUARIO ES USER (RESTRINGIDO)
        if rol == "USER":
            while True:
                print("\n==============================")
                print("Bienvenido")
                print(f"\n{nombre_usuario}")
                print("\nTipo de usuario:")
                print("USER")
                print("\n1. Cerrar sesión")
                print("==============================")
                
                opcion = input("Opción: ")
                if opcion == "1":
                    print("Cerrando sesión... Volviendo al Login.")
                    break  # Rompe este menú y vuelve a pedir Login
                else:
                    print("Opción inválida.")
                    
        # 3. MENU SI EL USUARIO ES ADMIN
        elif rol == "ADMIN":
            while True:
                print("\n==============================")
                print("       MENÚ ADMINISTRADOR     ")
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
                    print("Cerrando sesión... Volviendo al Login.")
                    break  # Rompe este menú y vuelve a pedir Login
                else:
                    print("Opción inválida. Intente de nuevo.")