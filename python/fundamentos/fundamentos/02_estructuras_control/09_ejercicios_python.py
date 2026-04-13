

#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuántos pares deseas ver?: "))
    pares = []
    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificarEdad():
 nacimiento = input("Ingrese su año de nacimiento: ")
 edad = 2026 - int(nacimiento)

 if edad >= 18:
    print()
    print("Eres nayor de edad ")
    print(f"Tienes {edad} años.")
 else:
    edadFaltante = 18 - edad
    print("Eres menor de edad.")
    print(f"Tienes {edad} y te faltan {edadFaltante} para ser mayor de edad.")


#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuento():
    precio = float(input("Ingresar precio del producto: "))
    cantidad = int(input("Ingresar cantidad:"))
    producto = precio * cantidad
    if producto >= 100:
     descuento = producto * 0.15
    else:
     descuento =  0
    total = producto - descuento
    print(f"El subtotal del producto es: {producto}, el descuento aplicado es: {descuento} y el total seria {total}")


#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
def clasificadorNum():
   num = int(input("Ingresa un número: "))
   if(num > 0):
# par
     if num % 2 == 0:
        print("Positivo-par")
     elif num % 2 == 0:
        print("Positivo-impar")
#Impar
     elif num < 0:
      if  num % 2 == 0:
        print("Negativo-par")
      elif num % 2 == 0:
        print("Negativo-impar")
      else:
        print("El número es 0")

#II. Iteraciones y Bucles (Intermedio)
#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.

def tablaMultiplicar():
   num = int(input("Ingresar número a trabajar: "))
   for i in range(1, 13):
      resultado = num * i
      if resultado % 3 == 0:
         print(f"del {num} los números que son divisibles por 3 son: {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
def sumatoriaCentinela():
   sumatotal = 0
   while True:
    n = int(input("Ingresar un número (negativo para salir): "))
    if n < 0:
       break
    sumaTotal += n
    print(f"La suma total es: {sumatotal}").lower()

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

def contadorVocales():
   texto = input("Ingresa una palabra o frase: ").lower
   for i in range(len(texto)):
      if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i]== "u":
         vocales += 1
      if texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
         print(f"La cadena {texto} tiene {vocales} vocales en total.")

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.

def validarContraseña():
   contraseña = "1234"
   intentos = 1
   while True:
      ingresa = input("Ingresar contraseña: ")
      if ingresa ==  contraseña:
         print("Acceso concedido")
         break
      else:
         intentos += 1
         if intentos > 3:
            print("Acceso denegado ")
            break 
         else:
            print(f"Número de intentos: {intentos}")
            
#III. Manejo de Arreglos / Listas (Avanzado)
#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

def registroNombres():
   nombres = []
   maxi = 0

   while maxi < 5:
      inp = input(f"Por favor ingresar nombre {maxi + 1}: ")
      if inp != "":
         nombres.append(inp)
      else:
         print("Tienes que ingresar un nombre")
      maxi += 1
      for i in range(4,-1, -1):
            print(nombres[i])

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

def promedioNotas():
   cantidad = int(input("¿Cuántas notas desea ingresar: "))
   nota = []
   for i in range(cantidad):
      nota = float(input(f"Nota {i+1}: "))
      nota.append(nota)

      promedio = sum(nota) / len(nota)
      print(f"Promedio: {promedio}")
      print(f"Nota más alta: {max(nota)}")
      print(f"Nota mas baja: {min(nota)}")

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

def filtroArreglos():
   cantidad = int(input("¿Cuantos números desea ingresar?: "))
   mayor50 = []
   nUser = []
   for i in range(1, cantidad):
      arrayUsuario = int(input("Ingrese un número: "))
      if arrayUsuario > 50:
         mayor50.append(arrayUsuario) 
      else: 
         nUser.append(arrayUsuario)
         print(f"Valores ingresado por el usuario: {nUser} \nValores mayor a 50: {mayor50} ")

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.

def buscadorElemento():
   ciudades = ["Nairobi", "Tokio", "Santiago", "Lima", "Caracas",  "Rio",  "Berlin",  "Seul",  "Buenos aires", "Denver"]
   ciudad = input("Ingresar ciudad: ").capitalize()
   esta = ciudades.index(ciudad)
   if esta < len(ciudades):
      print(f"Tu ciudad esta en el arreglo, en la posicion: {esta}")
   else:
      print("Tu ciudad no está en el arreglo")



#IV. Retos de Lógica Combinada
#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

def inventario():
    nombreProductos = []
    precios = []
    if i in range(3):
       nombre = input("Nombre del producto")
       precio = float(input("Precio: "))
       nombreProductos.append(nombre)
       precios.append(precio)
       print("\nInventario: ")
       for i in range(3):
        print(f"Producto: {nombreProductos[i]} - precio {precios[i]}")


#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).



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
    print("\n---8.- Ejercicio 8---")
    print("\n---9.- Ejercicio 9---")
    print("\n---10.- Ejercicio 10---")
    print("\n---11.- Ejercicio 11---")
    print("\n---12.- Ejercicio 12---")
    print("\n---13.- Ejercicio 13---")
    print("\n---14.- Ejercicio 14---")
    print("\n---15.- Ejercicio 15---")
    opcion = input("\n---- Elige una opción: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2:")
        print(verificarEdad())
    elif opcion == "3":
        print("\nEjecutando ejercicio 3:")
        print(aplicarDescuento())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4:")
        print(clasificadorNum())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5:")
        print(tablaMultiplicar())
    elif opcion == "6":
        print("\nEjecutando ejercicio 6:")
        print(sumatoriaCentinela())
    elif opcion == "7":
        print("\nEjecutando ejercicio 7:")
        print(contadorVocales())
    elif opcion == "8":
        print("\nEjecutando ejercicio 8:")
        print(validarContraseña())
    elif opcion == "9":
        print("\nEjecutando ejercicio 9:")
        print(registroNombres())
    elif opcion == "10":
        print("\nEjecutando ejercicio 10:")
        print(promedioNotas())
    elif opcion == "11":
        print("\nEjecutando ejercicio 11:")
        print(filtroArreglos())
    elif opcion == "12":
        print("\nEjecutando ejercicio 12:")
        print(buscadorElemento())
    elif opcion == "13":
        print("\nEjecutando ejercicio 13:")
        print(inventario())

    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no válida, intentar otra vez")
