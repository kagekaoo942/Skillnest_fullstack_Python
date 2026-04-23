import os
#Funciones básicas practica 2
#ejercicio 1
# Calcula experiencia
def ejercicio1(num):
    result = []
    for i in range (num + 1):
        result.append(i * 2)
        return result 
result1 = ejercicio1(5)
print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


#ejercicio 2
# Analiza publicaciones

def suma_y_resta(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma: {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"Retorno de resta = {resta}")
# Imprime: 235 y retorna: 5


#ejercicio 3
# Puntaje ajustado

def sumatoria_menos_longitud(sumatoria):
   sumatoria
   total = sum(sumatoria)
   longitud = len(sumatoria)
   resultado = total - longitud
   print(f"Total = {total}, longitud = {longitud}")
   

def ejercicio3():
   retornar = sumatoria_menos_longitud([10, 5, 3, 7])
   print(f"El resultado del retorno es: {retornar}")

# Suma total = 25, longitud = 4, debe retornar: 21
#ejercicio 4
# Ajusta visualizaciones
def valor_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    segEl = lista[1]     
    nuevaLista = []
    for i in lista:
        nuevaLista.append(i * segEl)
        long = len(nuevaLista)
        print(long)
        return nuevaLista


def ejercicio4():
    result1 = valor_multiplicados_segundo([100, 3, 50, 20])
    print(result1)
    print()
# Imprime: 4 y retorna: [300, 9, 150, 60]
result2 = valor_multiplicados_segundo([100])
print(result2)
# Imprime: 1 y retorna: [] 

# ejercicio 5
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range(0, b):
        multList.append(a * b)
        return multList


def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"resultado 1: {result1}")
    #Debe retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"Resultado 2: {result2}")
    #Debe retornar:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               [35, 35, 35, 35, 35]
#ejercicio 6
# Genera precio fijo
def ejercicio6():
    pass
ejercicio6(5, 2)
# Debe retornar: [10, 10]



#ejercicio 7
def ejercicio7():
    pass
ejercicio7(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')


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
    print("\n---7.- Ejercicio 7---")
    opcion = input("\n---- Elige una opción: (1-7) (0 para salir) =")
    if opcion == "1":
        limpiar_consola
        print("\nEjecutando ejercicio 1:")
        print(ejercicio1())
    elif opcion == "2":
        limpiar_consola
        print("\nEjecutando ejercicio 2:")
        print(ejercicio2())
    elif opcion == "3":
        limpiar_consola
        print("\nEjecutando ejercicio 3:")
        print(ejercicio3())
    elif opcion == "4":
        limpiar_consola
        print("\nEjecutando ejercicio 4:")
        print(ejercicio4())
    elif opcion == "5":
        limpiar_consola
        print("\nEjecutando ejercicio 5:")
        print(ejercicio5())
    elif opcion == "6":
        limpiar_consola
        print("\nEjecutando ejercicio 6:")
        print(ejercicio6())
    elif opcion == "7":
        limpiar_consola
        print("\nEjecutando ejercicio 7:")
        print(ejercicio7())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("Opcion no válida, intentar otra vez")