

#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuántos números pares deseas ver?: "))
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
    print("Eres nayor de edad ")
    print(f"Tienes {edad} años.")
 else:
    edadFaltante = 18 - edad
    print("Eres menor de edad.")
    print(f"Tienes {edad} y te faltan {edadFaltante} para ser mayor de edad.")


#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.

precioProducto = input("Ingresar precio del producto: ")
cantidadProducto = input("Ingrese la cantidad comprada:" )
precioFinal = precioProducto + cantidadProducto

if precioFinal > 100:
    print("Aplicar 15% de descuento")
    subTotal = precioProducto * cantidadProducto
    print(f"Su subtotal es {subTotal}")
    descuento = precioFinal * 15 / 100
    print(f"Su descuento es {descuento}")
    print(f"El precio final de su producto es {precioFinal}")
else:
    print("No se le aplica descuento")




#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
num = input("Ingrese un número")

#Cero
if num == 0:
    print("El número es cero") 

#Positivo
elif num > 0:
    if num % 2 == 0:
        print("El numero es positivo-Par")
    else:
        print("El número es positivo-Impar") 

#Negativo
else:
    if num % 2 == 0:
        print("El número es negativo-Par")
    else:
        print("El número es negativo-Impar")

     



#II. Iteraciones y Bucles (Intermedio)
#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.

#III. Manejo de Arreglos / Listas (Avanzado)
#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.

#IV. Retos de Lógica Combinada
#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

