# menu.py
from usuario import registrar_usuario, listar_usuarios

while True:
    print("\n1. Registrar | 2. Listar | 3. Salir")
    opcion = input("Opción: ")
    
    if opcion == "1":
        registrar_usuario()   # Llama a la función simplificada
    elif opcion == "2":
        listar_usuarios()      # Llama a la función simplificada que imprime con las barras '|'
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")