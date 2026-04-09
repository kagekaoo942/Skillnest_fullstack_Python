'''
Actividad: Gestor de inventario
'''

'''
 1.- Creación: Crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "raton" , "monitor", "cable hdmi"'''
inventario = ["laptop", "raton" , "monitor", "cable hdmi"]

'''2.- Expansión: Utiliza el método correspondiente para agregar "impresora" y "teclado" al final de la lista'''
inventario.append("impresora")
inventario.append("teclado")

'''3.- conteo: Utilixa la funcion integrada para mostrar cuantos elementos totales hay en la lista.'''
print(len(inventario))
'''4. Acceso y modificación: Modifica "teclado mecanico"'''
inventario[5] = "Teclado mecánico" 

''' 5.- Slicing: Crea una nueva lista llamada "promoción",
 debe contener solo 3 primeros elementos de la lista "articulos'''
promocion = inventario
print(f"Lista promocion: {promocion[:4]}")

''' 6.- Mostrar la lista de inventario ordenado alfabeticamente. '''
inventario.sort()
print(inventario)

''' 7.- Elimina el último elemento de la lista inventario mostrando el elemento 
eliminado y la lista final'''
eliminado = inventario.pop()
print("Articulo eliminado",eliminado)
print(inventario)

