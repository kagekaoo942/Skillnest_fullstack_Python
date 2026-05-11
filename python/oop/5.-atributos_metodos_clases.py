#Atributos, metodos de clases y metodos estáticos

#Definicion de la clase

class estudiante:
     #Atributo de la clase
     colegio = "liceo vate vicente huidobro"
     #Lista en donde esten todos los estudiantes
     estudiantes = []

     #Método constructor
     def _init_(self, nombre, nota):
          #Atributos de instancia
          self.nombre = nombre
          self.nota = nota
          #Agregar elementos a la lista estudiante(objeto)
          estudiante.estudiantes.append(self)

    #Metodo de instancia

def mostrar_info(self):
     print(f"Nombre: {self.nombre}")
     print(f"Nota: {self.nota}")

#Métodos de clase
# Usa "cls" porque trabaja con la información de la clase
@classmethod
def cambiar_colegio(cls, nuevo_nombre):
     #Accede a colegio eh inserta nuevo_nombre
     cls.colegio = nuevo_nombre
@classmethod #Contar la cantidad de estudiantes existentes
def cantidad_estudiante():
     return len(cls.estudiantes)
     
     #Metodo estatico
     #Este no usa CLS ni SELF, solo parámetros.
@staticmethod

def aprobar(nota):
          if nota >= 4.0:
            return True
          else:
               return False
          
#Creacion de objetos(instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 6.7)

#Usar atributo de la clase
print("== Atributo de clase ==")
print(e1.colegio)
print(e2.colegio)
print()


#Uso de métodos de instancias
print("== Método de instancia==")
#Mostrar datos de estudiante
e1.mostrar_info()
print()
e2.mostrar_info()
print()

#Uso de método de clase
print("=== Método de clase ===")
Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
print(e2.colegio)

#Contar Estudiantes
print("=== Contar estudiantes===")
print(f"Total de estudiantes: {Estudiante.cantidad_estudiantes()}")


#Método estático
print("=== Método estatico ==")


## Función repaso.
## Crear una función que valide usuario y contraseña
def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(F"Bienvenido, {user}!")
        return True
    else:
        print("Acceso denegado")
        return False
    
def enviarDatos():
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        validador(username, password) 
enviarDatos()
