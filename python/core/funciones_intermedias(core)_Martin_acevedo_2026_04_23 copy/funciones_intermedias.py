# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

#Parte 1:
#1. En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda). Resultado esperado:
puntajes[2][0] = 600
'''
2. En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
En ubicacion, cambia el valor de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).
'''
streamers[0]["GameNinjaPro"] = "EliteGamerX"
eventos[0]["Las Vegas"] = "San Fracisco"
ubicacion[0]["Latitud"] = 40.712776

#Parte 2
'''
1. Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers) y recorra cada uno, imprimiendo sus claves y valores.
Formatea la salida para que cada diccionario se imprima en una sola línea, con el formato.
'''
#2. Obtener valores de un diccionario creando la función obtener_valores(clave, lista) que reciba, por una parte, una cadena con el nombre de una clave, por otra, una lista de diccionarios. La función debe imprimir el valor asociado a esa clave en cada uno de los diccionarios.
def obtener_valores(clave, lista):
 if clave in s



#Valores esperados:
#EliteGamerX
#PixelWarrior

#250000
#180000

#Parte 3:


 '''
 Crea la función mostrar_informacion(diccionario), que reciba un diccionario en el que los valores sean listas. La función debe, por una parte, imprimir el tamaño de la lista y la clave en mayúsculas, por otra, imprimir cada elemento de la lista en líneas separadas.
 Ejemplo de uso:
 '''

'''
categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

mostrar_informacion(categorias)​
'''

'''
Salida esperada:
4 JUEGOS_POPULARES
Fortnite
Minecraft
Valorant
GTA V

3 CIUDADES_EVENTOS
Nueva York
Madrid
Tokio​
'''

#🎯 MINI DESAFÍO (nivel core)
datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(f"Nombre: {datos[2]["nombre"]} - {datos[2]["puntaje"]}")

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"

def cambiarPuntaje():
    print(f"Nombre: {datos[0]["nombre"]} - Obtuvo: {datos[0]["puntaje"]} puntos")

    cambiarPuntaje()

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def imprimirDatos(nombre): 
    if nombre == "María":
        print(f"Nombre: {nombre} - puntaje: {datos[1]["puntaje"]} puntos")

imprimirDatos()
print(f"Nombre: {datos[1]["nombre"]}")


