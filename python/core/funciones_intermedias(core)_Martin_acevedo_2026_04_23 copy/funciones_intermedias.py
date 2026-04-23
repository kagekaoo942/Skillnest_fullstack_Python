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
streamers[0]["nombre"] = "EliteGamerX"
eventos["Estados Unidos"][2] = "San Francisco"  
ubicacion[0]["latitud"] = 40.712776

#Parte 2
'''
 1. Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers) y recorra cada uno, imprimiendo sus claves y valores.
 Formatea la salida para que cada diccionario se imprima en una sola línea, con el formato.
'''
def iterar_diccionario(lista):
    for diccionario in lista:
        print(f"{diccionario['nombre']}: {diccionario['seguidores']}")
def obtener_valores(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])

#2. Obtener valores de un diccionario creando la función obtener_valores(clave, lista) que reciba, por una parte, una cadena con el nombre de una clave, por otra, una lista de diccionarios. La función debe imprimir el valor asociado a esa clave en cada uno de los diccionarios.
def obtener_valores(clave, lista):
    """
    Recorre una lista de diccionarios e imprime el valor 
    asociado a la clave proporcionada.
    """
    for diccionario in lista:
        # Verificamos si la clave existe en el diccionario para evitar errores
        if clave in diccionario:
            print(diccionario[clave])
        else:
            print(f"La clave '{clave}' no se encuentra en este diccionario.")

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
def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        # Se imprime la longitud y la clave en mayúsculas y separadas por espacio
        print(f"{len(lista)} {clave.upper()}")
        
        # Se recorre la lista para imprimir cada elemento
        for elemento in lista:
            print(elemento)
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