import random

"""
Este archivo sirve para practicar la ejecución de archivos en Python.
Incluimos un ejemplo con un bucle y selección aleatoria de días,
para que te familiarices con la terminal y el flujo básico de un programa.
"""

# Imprimimos un mensaje de bienvenida
print("¡Bienvenido a Python!")

# Explicamos lo que haremos a continuación
print("Ahora veremos un bucle que muestra los números del 1 al 10:")

# Bucle for que recorre los números del 1 al 10
num = int(input("Ingrese un numero limite: ")) # es como un parseInt()
for num in range(1, num + 1):
    print(f"El valor actual de num es: {num}")

# Definimos una lista de días laborables
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Seleccionamos al azar un día de la semana
dia = random.choice(semana)
# f es para concatenar el string con la varible dia
print(f"Hoy es: {dia}")

# Si es sabado o domingo imprimir("Descansa todo lo que puedas!")
# Dependiendo del día, mostramos un mensaje motivacional distinto
if dia == "Lunes":
    print("¡Comenzamos la semana con buena energía!")
elif dia == "Viernes":
    print("¡Cerramos la semana listos para un buen descanso!")
elif dia == "Sabado" or dia =="Domingo":
    print("Descansa todo lo que puedas!") 
else:
    print("¡Cada día es una nueva oportunidad de aprender!")

