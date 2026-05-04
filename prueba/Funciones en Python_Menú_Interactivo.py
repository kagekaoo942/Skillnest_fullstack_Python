import os
#Ejercicio 1: Crear una función que reciba una lista de números enteros y genere una nueva lista solo con los números pares mayores a 10.
#  Luego debe mostrar la nueva lista y la cantidad de elementos encontrados.

# Función que devuelve una lista de números pares mayores a 10
def numerosPares(lista):
    # Inicia con una lista vacía para almacenar los números pares
    numero = []
    # bucle sobre la lista de números
    for i in range(len(lista)):
        # Verifica si el número es par y mayor a 10
        if lista[i] % 2 == 0 and lista[i] > 10:
            # Agrega el número a la lista de números pares
            numero.append(lista[i])
    # Devuelve la lista de números pares
    return numero
# Función que llama a la función numerosPares y imprime el resultado
# Función principal para interactuar con el usuario
def ejercicio1():
    # Inicializa una lista vacía para guardar las entradas del usuario
    lista = []

    # Solicita al usuario la cantidad de números y lo convierte a entero
    num_elementos = int(input("Ingrese la cantidad de números que desea ingresar: "))

    # Bucle que se repite la cantidad de veces definida anteriormente
    for i in range(num_elementos):
        # Se solicita el número, indicando visualmente cuál posición se está llenando
        num = int(input(f"Ingrese el número {i+1}: "))
        # Agrega el número ingresado a la lista principal
        lista.append(num)

    # Llama a la función 'numerosPares' pasando la lista llena y guarda el retorno
    nuevaLista = numerosPares(lista)
    # Muestra en consola la nueva lista filtrada
    print(nuevaLista)
    
    # Muestra un mensaje con el conteo de elementos (longitud) de la nueva lista
    print(f"La cantidad de elementos encontrados en la lista es: {len(nuevaLista)}")

# Punto de entrada: Ejecuta la función principal para que el programa inicie
ejercicio1()

def limpiar_consola():
    os.system('cls')
#Menu de navegacion para ejercicios
continuar = True
while continuar:
    print("\n--- Ejercicios Python---")
    print("\n---1.- Ejercicio 1---")
    opcion = input("\n---- Elige una opción: (1-2) (0 para salir) =")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1:")
        print(ejercicio1())

    elif opcion == "2":
        limpiar_consola
        print("\nEjecutando ejercicio 2:")
        print(ejercicio2())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("Opcion no válida, intentar otra vez")
