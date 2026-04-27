#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar


#Creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la,",10000,0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000,20000)
martin = Usuario("Martin", "Acevedo", "marti@codingdojo.la", 30000, 200)
#Imprimimos los valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

'''
Crear una clase Estudiante y asignarle los siguientes atributos: 
(rut, nombre, apellido, especialidad, fecha_nac)
Crear 3 instancias para la clase con distintos Estudiantes.
Imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
    def _init_(self, rut, nombre, apellido, email, especialidad, fecha_nac):
        pass
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

carla = Estudiante("22.368.905-4", "Carla", "Menedez", "carla@gmail.com", "Programacion", "22/05/2006")
carlos = Estudiante("22.572.245-1", "Carlos", "Menedez", "carla@gmail.com", "Programacion", "05/10/2008")
fernando = Estudiante("24.265.365-4", "Carla", "Menedez", "carla@gmail.com", "Programacion", "23/02/2007")

print(carla.nombre)
print(carlos.nombre)
print(fernando.nombre)

