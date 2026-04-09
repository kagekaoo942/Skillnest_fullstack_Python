"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importacion de libreria de procesos aleatorios

nombre = "Frida Kahlo" # crecacion de una variable tipo string y se asigna un valor 
print(type(nombre)) # type() = metodo que muestra el tipo de una variable 
print(len(nombre)) # len() = devuelve el largo de una variable


edad = 25 # creacion de variable tipo numerico(int)


if edad < 18: # Se establece una condición if
   print("Eres menor de edad.") # imprime un mensaje 
elif edad == 18: # se crea subcondicion elif(else if) 
   print("Tienes 18 años.") # imprime un mensaje
else: # cierra de condicion (si no se cumplen condiciones anteriores)
   print("Eres mayor de edad.") # imprime un mensaje 


frutas = ["manzana", "pera", "fresa"] # se crea un array con valores ya asignados
print(frutas[0]) # muestra la primera posicion del array
frutas[0] = "banana" # A la posicion del arreglo se le asigna el valor de "banana"
frutas.append("uva") # Se le agrega "uva" al final del array
frutas.remove("pera") # Se remueve "pera" del arreglo

dimensiones = (200, 50) # Creacion de una variable de tipo tupla (variable inmutable)
print(dimensiones[0]) # Se imprime la posición 0 de la varible creada

persona = { "" # Variable tipo object(objetc)
   "nombre": "Carlos", # Se establece un item y su respectivo valor 
   "edad": 30 # Se establece un item y su respectivo valor 
}
print(persona["nombre"]) # imprime el valor de item(ej: "Carlos")
persona["edad"] = 31 # Se modifica el valor del item edad  a 31
persona["ciudad"] = "Santiago" # Se agrega un nuevo item con un valor
del persona["ciudad"] # Se elimina el item completo

for i in range(5): #for range: Se crea bucle en rango desde 0 a 5
    if i == 2: # Se establece condicion if == 2
       continue # continue: ignora el proceso y continua
    if i == 4: # Se establece condicion if i == 4
       break # Si i = 4 se rompe el bucle
    print(i) # Imprime el valor de i en cada iteracion.(hasta 4)


contador = 0 # Se crea una variable contador tipo númerica(int)
while contador < 3: # Se crea bucle While con una condición
   print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con f"" string
   contador += 1 # Incrementa el valor en 1 en cada iteración


def saludar_usuario(nombre): # def: Palabra reservada para crear una función
   return f"Hola, {nombre}" # Devuelce un valor de la función


print(saludar_usuario("Francisca")) # Se imprime "Hola Fracisca" - return de la función

