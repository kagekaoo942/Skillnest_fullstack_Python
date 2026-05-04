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
def ejercicio1():
    # Se crea una lista de números
    lista = [1, 2, 3, 11, 12, 13, 14, 15, 16]
    # Llama a la función numerosPares y almacena el resultado en nuevaLista
    nuevaLista = numerosPares(lista)
    # Imprime la lista de números pares
    print(nuevaLista)
    # Imprime la cantidad de elementos en la lista de números pares
    print(f"La cantidad de elementos encontrados en la lista es: {len(nuevaLista)}")

# Llama a la función ejercicio1
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
