"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

def generarNiveles():
    for nivel in range(0, 101):
        print(f"Nivel {nivel}")
# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)


def generarPotenciador():
    for numero in range(2, 500, 2):
        print(f"Potenciador de energía: {numero}")
# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""2
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)
def trampaEmojis():
    for puntos in range(1, 100):
        if puntos % 10 == 0:
            print("💣")
        elif puntos % 5 == 0:
            print("⚠️")
        else:
            print(puntos)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)
def sumaColosal():
    sumaTotal = 0
    for numero in range(0, 500000, 2):
        sumaTotal += numero
    print(f"Suma total de números pares del 0 al 500,000: {sumaTotal}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)
def retrocesoTemporal():
    for año in range(2024, -1, -3):
        print(f"Año retrcedido: {año}")

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)
def contadorDinamico():
    numeroInicial = int(input("Ingrese el número inicial: "))
    numeroFinal = int(input("Ingrese el número final: "))
    salto = int(input("Ingrese cuanto debe saltar: "))
    for numero in range(numeroInicial + salto, numeroFinal + 1, salto):
        print(f"Número en el rango: {numero}")
# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

#Menu de navegacion para ejercicios
continuar = True
while continuar:
    print("\n--- Ejercicios Python---")
    print("\n---1.- Ejercicio 1---")
    print("\n---2.- Ejercicio 2---")
    print("\n---3.- Ejercicio 3---")
    print("\n---4.- Ejercicio 4---")
    print("\n---5.- Ejercicio 5---")
    print("\n---6.- Ejercicio 6---")
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        print(generarNiveles())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2:")
        print(generarPotenciador())
    elif opcion == "3":
        print("\nEjecutando ejercicio 3:")
        print(trampaEmojis())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4:")
        print(sumaColosal())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5:")
        print(retrocesoTemporal())
    elif opcion == "6":
        print("\nEjecutando ejercicio 6:")
        print(contadorDinamico())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no válida, intentar otra vez")