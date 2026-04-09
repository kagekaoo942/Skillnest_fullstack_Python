# Diccionarios en Python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
# Imprimir el nombre del estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Gonzalo

#Diccionario paises
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"

# Condicion para buscar elemento e insertar si no existe
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"

#Eliminar valores de diccionario
print(paises)
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print((f"Valor removido: {valor_removido}"))
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

print(paises)

#Diccionario Pintor nultilíneal
pintor = { "nombre": "Frida Kahlo", 
          "pais": "México", 
          "fecha_nacimiento": "6 de julio de 1907"
         }

#Diccionario anidados
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}
                            