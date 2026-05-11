'''
Actividad: Desarrollo de funciones en Python con distintos tipos de datos
Objetivo de aprendizaje
Desarrollar programas en Python utilizando funciones, estructuras de control, listas, diccionarios y distintos tipos de datos, aplicando lógica de programación para la resolución de problemas mediante el uso de menús interactivos y validación de información.

Instrucciones generales
Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input(). Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for, junto con estructuras condicionales como if, elif y else.
El programa deberá incluir una opción para salir correctamente del sistema.

'''
# Ejercicios a desarrollar
#Ejercicio 1
# Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor
#  y cuál es el menor.

def listaNumeros(listado):
    menor = min(listado) #Busca el elemento menor
    mayor = max(listado) #Busca el elemento mayor
    print()

def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = input(f"Ingresa un número entero {i} de {limit}: ")
        listadoNum.append(num)
        i+= 1
        listaNumeros(listadoNum)

#Ejercicio 2
# Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocales(letra):
 vocales = "aeiouAEIOU"
 for letra in vocales:
    return letra in vocales #Devuelve true si la letra está dentro de las vocales, sin no false
 
def contadorVocales(texto):
 contador = 0
 for letra in texto:
    if contadorVocales(letra):
       contador += 1
       print(f"La cadena contiene {contador} vocales.")


def ejercicio_contadorVocales():
          texto = input("Ingrese una cadena de texto: ")
          contadorVocales(texto)

def ejercicio_contadorVocales():
   pass
# Ejercicio 3
#Crear una función que reciba una lista de nombres y 
# muestre únicamente aquellos que tengan más de 5 letras.
def filtrar(lista):
 resultado = []
 for nombre in lista:

   if len(nombre) > 5:
      resultado.append(nombre)
      return resultado
   
def mostrar():
        nombres = []
        cantidad = int(input("¿Cuantos nombres quiere ingresar? "))

        for i in range(cantidad):
           nombre = input("Ingresar nombre")
           print(f"{nombre} agregado con exito a la lista.")
           nombre.append(nombre)

           listaNombres =  filtrar(nombres)
           print(f"Los nombres con más de 5 letras son: \n {("\n-").join(listaNombres)}")
mostrar()

# Ejercicio 4
#Crear una función que reciba una lista de notas (números decimales),
#calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def listaNotas(notas):
    lista = 0
    promedio = 0 
    for i in range(len(notas)):
        lista += notas[i]
        promedio = lista / (len(notas))
        if notas[i] >= 4.0 and notas[i] <= 7.0:
            print(f"El estudiante aprueba con {promedio}")
        elif notas[i] >= 1.0 and notas[i] <= 3.9:
            print(f"El estudiante no aprueba con {promedio}")
        else:
            return "Error"

def ejercicio4():
    largo =  int(input("Cuantas notas va a ingresar: "))
    nota = []
    for i in range(largo):
        inp = float(input(f"Ingrese nota {i + 1}: "))
        if inp != "":
            nota.append(inp)
    print(listaNotas(nota))
ejercicio4()

# Ejercicio 5
#Crear una función que reciba una lista de precios de productos
# y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.

def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * (90 / 100)
    precioFinal = precioFinal - descuento
    print(f"El precio inicial del producto es: \n{precioInicial} y con descuento: \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiera:\n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto:\n"))
        listaPrecios.append(valorProducto)
        descuento(listaPrecios)

valores()

# Ejercicio 6
#Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es Par.")
    elif numero % 3 == 0:
        print(f"El número {numero} es Impar.")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingresar número: "))
    parImpar(num)
recibirNum()


# Ejercicio 7
#Crear una función que reciba una lista de edades 
# y muestre cuántas personas son mayores de edad (18 años o más).

def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            if lista[i] >= 18:
                num += 1
    return num

def personas():
    edad = []
    inp = int(input("Cuantos personas vas a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var != "":
            edad.append(var)
        else:
            print("Por favor ingresar valor válido")
            resultado = edades(edad)
            print(f"hay {resultado} oersibas mayores de edad")
personas()




# Ejercicio 8
#Crear una función que reciba una lista de palabras 
# y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def vecesAparece(palabra):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesAparece = 0
    for i in range(len(palabra)):
        if buscar == palabra[i]:
            vecesAparece += 1
            print(f"La palabra {buscar} aparece {vecesAparece} en la lista. ")

def recibirPalabra():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listaPalabras.append(palabra)
        vecesAparece(listaPalabras              )


# Ejercicio 9
#Crear una función que reciba una lista de números y
#  genere una nueva lista que contenga únicamente los números positivos. 
    


# Ejercicio 10
#Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) 
# y muestre cuáles tienen un stock menor a 5 unidades.

#Requisitos obligatorios

'''
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)


Forma de entrega
Debe subir un único archivo .py correctamente identificado con su nombre y apellido.
Ejemplo:
apellido_nombre_funciones.py

Criterios de evaluación
Se evaluará:
Correcto funcionamiento de las funciones
Aplicación adecuada de estructuras de control
Uso correcto de listas y diccionarios
Lógica de programación
Orden, claridad e indentación del código
Cumplimiento de todos los requerimientos solicitados
'''
